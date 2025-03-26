import random

def best_selection(population, maximize):
    if maximize:
        sorted_population = sorted(population, key=lambda x: x.fitness, reverse=True)
    else:
        sorted_population = sorted(population, key=lambda x: x.fitness)

    return sorted_population[:3]

def tournament_selection(population, tournament_size, maximize):
    tournament = random.sample(population, tournament_size)
    if maximize:
        return max(tournament, key=lambda x: x.fitness)
    else:
        return min(tournament, key=lambda x: x.fitness)

def roulette_selection(population, maximize):
    if maximize:
        total_fitness = sum(ind.fitness for ind in population if ind.fitness > 0)
    else:
        total_fitness = sum(1.0 / ind.fitness for ind in population if ind.fitness > 0)

    pick = random.uniform(0, total_fitness)
    current = 0
    for ind in population:
        if ind.fitness > 0:
            if maximize:
                current += ind.fitness
            else:
                current += 1.0 / ind.fitness

            if current > pick:
                return ind

