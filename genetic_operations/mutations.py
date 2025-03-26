import random


def boundary_mutation(chromosome):
    chromosome.genes[0] = 1 - chromosome.genes[0]
    chromosome.genes[-1] = 1 - chromosome.genes[-1]

def one_point_mutation(chromosome):
    index = random.randint(0, len(chromosome.genes) - 1)
    chromosome.genes[index] = 1 - chromosome.genes[index]

def two_point_mutation(chromosome):
    index1, index2 = sorted(random.sample(range(len(chromosome.genes)), 2))
    chromosome.genes[index1] = 1 - chromosome.genes[index1]
    chromosome.genes[index2] = 1 - chromosome.genes[index2]