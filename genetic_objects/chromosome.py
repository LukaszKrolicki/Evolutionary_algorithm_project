import random
from optimization_functions import martin_gaddy
import random

class Chromosome:
    def __init__(self, length, begin_range=-20, end_range=20):
        self.genes = [random.choice([0, 1]) for _ in range(length)]
        self.fitness = None
        self.begin_range = begin_range
        self.end_range = end_range

    def decode(self):
        mid = len(self.genes) // 2
        x1 = int("".join(map(str, self.genes[:mid])), 2) / (2 ** mid - 1) * (self.end_range - self.begin_range) + self.begin_range
        x2 = int("".join(map(str, self.genes[mid:])), 2) / (2 ** mid - 1) * (self.end_range - self.begin_range) + self.begin_range
        return x1, x2

    def evaluate(self):
        x, y = self.decode()
        self.fitness = martin_gaddy(x, y)

    def clone(self):
        clone = Chromosome(len(self.genes), self.begin_range, self.end_range)
        clone.genes = self.genes[:]
        clone.fitness = self.fitness
        return clone