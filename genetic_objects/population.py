from genetic_objects.chromosome import Chromosome

class Population:
    def __init__(self, population_size, precision):
        self.individuals = [Chromosome(2 * precision) for _ in range(population_size)]
        for individual in self.individuals:
            individual.evaluate()  
