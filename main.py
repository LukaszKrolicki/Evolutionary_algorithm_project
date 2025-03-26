import random
import time

from genetic_operations.crossovers import one_point_crossover, two_point_crossover, uniform_crossover, granular_crossover
from genetic_operations.mutations import boundary_mutation, one_point_mutation, two_point_mutation
from genetic_objects.population import Population
from genetic_operations.selections import tournament_selection, best_selection, roulette_selection
from genetic_operations.strategies import inversion
from visualization.visualization import save_results


CROSSOVER_METHODS = {
    "one_point": one_point_crossover,
    "two_point": two_point_crossover,
    "uniform": uniform_crossover,
    "granular": granular_crossover
}

MUTATION_METHODS = {
    "boundary": boundary_mutation,
    "one_point": one_point_mutation,
    "two_point": two_point_mutation
}


def run_algorithm(population_size, precision, num_epochs, selection_method,
                  crossover_method, mutation_method, elitism, mutation_rate, crossover_probability,
                  inversion_probability, begin_range, end_range, select_best_amount, tournament_size, maximize):
    start_time = time.time()
    population = Population(population_size, precision)
    history = []
    fit_hist = []
    operations = []

    crossover_func = CROSSOVER_METHODS[crossover_method]
    mutation_func = MUTATION_METHODS[mutation_method]

    for epoch in range(num_epochs):
        new_population = []

        if elitism > 0:
            elites = sorted(population.individuals, key=lambda x: x.fitness, reverse=maximize)[:elitism]
            new_population.extend(elites)

        while len(new_population) < population_size:
            if selection_method == "select_best":
                selected_parents = best_selection(population.individuals, maximize)
                parent1, parent2 = selected_parents[0], selected_parents[1]
            elif selection_method == "tournament":
                parent1 = tournament_selection(population.individuals, tournament_size, maximize)
                parent2 = tournament_selection(population.individuals, tournament_size, maximize)
            elif selection_method == "roulette":
                parent1 = roulette_selection(population.individuals, maximize)
                parent2 = roulette_selection(population.individuals, maximize)

            operations.append({"epoch": epoch, "type": "selection", "parents": (parent1.decode(), parent2.decode())})

            if random.random() < crossover_probability:
                child1, child2 = crossover_func(parent1, parent2)
                operations.append({"epoch": epoch, "type": "crossover", "children": (child1.decode(), child2.decode())})
            else:
                child1, child2 = parent1.clone(), parent2.clone()

            if random.random() < mutation_rate:
                mutation_func(child1)
                operations.append({"epoch": epoch, "type": "mutation", "child": child1.decode()})
            if random.random() < mutation_rate:
                mutation_func(child2)
                operations.append({"epoch": epoch, "type": "mutation", "child": child2.decode()})

            if random.random() < inversion_probability:
                inversion(child1)
                operations.append({"epoch": epoch, "type": "inversion", "child": child1.decode()})
            if random.random() < inversion_probability:
                inversion(child2)
                operations.append({"epoch": epoch, "type": "inversion", "child": child2.decode()})

            child1.evaluate()
            child2.evaluate()

            operations.append({"epoch": epoch, "type": "result children", "children": (child1.decode(), child2.decode())})

            new_population.extend([child1, child2])

        population.individuals = new_population[:population_size]
        final_population = [(ind.decode(), ind.fitness) for ind in population.individuals]
        final_population.sort(key=lambda x: x[1], reverse=maximize)
        operations.append({"epoch": epoch, "type": "final_population",  "population": final_population})

        best = max(population.individuals, key=lambda x: x.fitness) if maximize else min(population.individuals,
                                                                                         key=lambda x: x.fitness)
        history.append(best.decode())
        fit_hist.append(best.fitness)

    best_solution = best.decode()
    end_time = time.time()

    print(f"\nObliczenia dla:")
    print(f"📌 Populacja: {population_size}, Precyzja: {precision}")
    print(f"📌 Epoki: {num_epochs}, Selekcja: {selection_method}")
    print(f"📌 Krzyżowanie: {crossover_method}, Mutacja: {mutation_method}")
    print(f"📌 Współczynnik mutacji: {mutation_rate}, Prawdopodobieństwo inwersji: {inversion_probability}")
    print(f"📌 Prawdopodobieństwo krzyżowania: {crossover_probability}, Rozmiar turnieju: {tournament_size}")
    print(f"📌 Zakres: ({begin_range}, {end_range}), Maksymalizacja: {maximize}")
    print(f"📌 Wybór najlepszych: {select_best_amount}")

    print(f"\nCzas obliczeń: {end_time - start_time:.2f} seconds")
    print(f"Best fitness: {best.fitness}")
    print(f"Best solution (X, Y): {best_solution}")

    save_results(best_solution, history, fit_hist, operations,begin_range, end_range)

    return best.fitness
