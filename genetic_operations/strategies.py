import random

def inversion(chromosome):
    start, end = sorted(random.sample(range(len(chromosome.genes)), 2))
    chromosome.genes[start:end+1] = reversed(chromosome.genes[start:end+1])

def elitist_strategy(population, offspring, elite_size=1):
    return sorted(population + offspring, key=lambda x: x.fitness)[:len(population)]
