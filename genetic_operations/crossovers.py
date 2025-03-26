import random
from genetic_objects.chromosome import Chromosome

def one_point_crossover(parent1, parent2):
    point = random.randint(1, len(parent1.genes) - 1)
    child1 = Chromosome(len(parent1.genes))
    child2 = Chromosome(len(parent2.genes))
    child1.genes = parent1.genes[:point] + parent2.genes[point:]
    child2.genes = parent2.genes[:point] + parent1.genes[point:]
    return child1, child2

def two_point_crossover(parent1, parent2):
    point1, point2 = sorted(random.sample(range(1, len(parent1.genes)), 2))
    child1 = Chromosome(len(parent1.genes))
    child2 = Chromosome(len(parent2.genes))
    child1.genes = parent1.genes[:point1] + parent2.genes[point1:point2] + parent1.genes[point2:]
    child2.genes = parent2.genes[:point1] + parent1.genes[point1:point2] + parent2.genes[point2:]
    return child1, child2

def uniform_crossover(parent1, parent2):
    child1 = Chromosome(len(parent1.genes))
    child2 = Chromosome(len(parent2.genes))
    for i in range(len(parent1.genes)):
        child1.genes[i], child2.genes[i] = (parent1.genes[i], parent2.genes[i]) if random.random() < 0.5 else (parent2.genes[i], parent1.genes[i])
    return child1, child2

def granular_crossover(parent1, parent2, grain_size=2):
    child1 = Chromosome(len(parent1.genes))
    child2 = Chromosome(len(parent2.genes))
    for i in range(0, len(parent1.genes), grain_size):
        if random.random() < 0.5:
            child1.genes[i:i+grain_size] = parent1.genes[i:i+grain_size]
            child2.genes[i:i+grain_size] = parent2.genes[i:i+grain_size]
        else:
            child1.genes[i:i+grain_size] = parent2.genes[i:i+grain_size]
            child2.genes[i:i+grain_size] = parent1.genes[i:i+grain_size]
    return child1, child2