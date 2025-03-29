# Evolutionary_algorithm_project

Optimization of multi-variable functions is a classic problem in mathematics and computer science. It involves finding the best variable values (e.g., function minimum or maximum) in a multidimensional space. This approach is widely used in engineering and artificial intelligence.

The goal of this project is to implement a genetic algorithm for optimizing multi-variable functions.

## Theoretical Background

Genetic algorithms (GAs) are a class of optimization algorithms inspired by biological processes such as natural selection and genetics. They are used to find solutions in complex search spaces where traditional optimization methods may be inefficient.

Genetic algorithms operate by simulating the evolution process, where solutions (individuals) "compete" for survival and reproduction in an optimization problem.

Key elements of genetic algorithms:

Chromosomes – A chromosome represents a solution, typically encoded as a vector, bit string, or sequence of numbers/characters.

Genes – The smallest unit of information in a chromosome, representing a feature of the solution.

Population – A set of chromosomes representing different potential solutions. The population is initially generated randomly or based on some predefined rules.

Selection – Selection determines which chromosomes will reproduce. Several methods can be used:

Roulette wheel selection: Individuals are chosen based on their fitness function, where more "fit" individuals have a higher chance of being selected.

Tournament selection: Random individuals are selected, and the best among them is chosen for reproduction.

Best selection: The best individuals from the current generation are retained.

Crossover – After selecting parents, crossover is applied to generate new offspring. Various techniques exist:

Single-point crossover: One division point in the chromosome.

Two-point crossover: Two division points.

Uniform crossover: Each gene is randomly inherited from one of the parents.

Granular crossover: Similar to uniform, but entire blocks of genes are randomly selected.

Mutation – Random modification of genes to introduce diversity and improve solutions.

Elitism – Ensures that the best individuals always survive to the next generation.

Fitness Evaluation – Each chromosome is assessed using a fitness function, which determines how well it solves the optimization problem.

Reproduction Process – The algorithm iterates through multiple generations, applying selection, crossover, mutation, and fitness evaluation, until a satisfactory solution is found.

## Technologies Used

Python 3.11

tkinter

ttkbootstrap

matplotlib

## Project Components

Implementation of a genetic algorithm for function minimization.

Configurable number of variables.

Binary representation of chromosomes.

Graphical user interface (GUI).

Graph generation of function values across iterations.

Saving results to a file/database.

## Test Function

This project aims to find the minimum/maximum of the Martin and Gaddy function.

![image](https://github.com/user-attachments/assets/8ecdc5e8-ab0b-42f8-9cb7-a2a8ee3bc82e)


![image](https://github.com/user-attachments/assets/53a1b302-ecc1-452f-98cc-5ab23a3929d4)


## Chromosome Representation

![image](https://github.com/user-attachments/assets/ad55fed1-b543-4a49-b7e9-9fb2081a2bd5)

self.genes – Encodes the values.

self.fitness – Stores the fitness function value.

decode() – Converts a binary chromosome into real numbers. The first half represents variable X, and the second half represents Y, scaled to the range [-20, 20]:

Normalize the binary number to the range [0,1].

Scale it to [-20, 20].

evaluate() – Decodes the chromosome and computes the fitness function value. Lower fitness values indicate better solutions (for minimization problems).

## Population

![image](https://github.com/user-attachments/assets/99ab875b-fa39-485c-a3bc-2c0a64f4a1af)

The Population class generates a set of potential solutions. The Martin and Gaddy function has two variables, so the number of variables is fixed.

population_size – Number of individuals.

precision – Number of bits allocated for each variable.

## Selection

![image](https://github.com/user-attachments/assets/5f222d35-c291-4865-97bb-94fb48379cfa)

Tournament selection – Random individuals compete, and the best one is selected.

![image](https://github.com/user-attachments/assets/e5e16a54-32f5-4ddf-9dd9-482a1bc22a2f)

Best selection – Selects the best individuals.

![image](https://github.com/user-attachments/assets/a68f2a0b-b536-4f18-aa4f-0485af0c9750)

Roulette wheel selection – If maximizing, total fitness is the sum of all fitness values. For minimization, fitness is inverted, giving lower fitness values higher weights.

## Crossover

![image](https://github.com/user-attachments/assets/23d66361-8fe3-4c2c-af8b-d22cd3202a59)

Single-point crossover – A single division point in the chromosome.

![image](https://github.com/user-attachments/assets/25623bde-38ab-44b3-9981-9b3406ea1438)

Two-point crossover – Two division points.

![image](https://github.com/user-attachments/assets/de60846c-34c8-4304-8525-c58980ae924a)

Uniform crossover – Each gene is randomly selected from either parent.

![image](https://github.com/user-attachments/assets/0e90bb89-0f01-4203-bbd3-d4c4ab6e2451)

Granular crossover – Like uniform, but selects entire blocks.

## Mutation

![image](https://github.com/user-attachments/assets/d819cab9-449e-47fb-8ba3-ce8f1196d76b)

Boundary mutation – Flips the first and last gene.

![image](https://github.com/user-attachments/assets/b5aba293-6afc-4fe0-9081-9e24a65c4424)

Single-point mutation – Randomly selects and flips a gene.

![image](https://github.com/user-attachments/assets/b7944f09-bfed-4273-8bf8-3c62f2cf8491)

Two-point mutation – Selects two different genes and flips their values.

![image](https://github.com/user-attachments/assets/f90b333b-e433-45c7-a290-2e6b630e714e)

Inversion mutation – Selects a random segment and reverses its values.

## Algorithm Workflow

Iterate through epochs.

Create new_population to store selected and modified individuals.

Apply elitism and add the best individuals.

Generate the new population:

Apply crossover, mutation, inversion.

Evaluate fitness.

Add new individuals.

## GUI

The GUI, built using tkinter, allows users to configure and interact with the algorithm efficiently.

![image](https://github.com/user-attachments/assets/65b63830-fe5c-4237-afa3-848e0dc56284)

## Visualization and Program Execution

The program provides visualization of results using:

3D plot with the best solution.

Heatmap and an animated heatmap (GIF) showing the best solutions across epochs.

Fitness function plot.

Event log tracking algorithm operations.

## Example 1 – Tournament Selection

![image](https://github.com/user-attachments/assets/69cb0db6-c382-4ae4-bb09-baa67a98c5eb)

![image](https://github.com/user-attachments/assets/e22eb225-d7d9-4a13-af07-9153769f3a17)

![image](https://github.com/user-attachments/assets/ce6dd3de-132c-4ccb-b5c8-986dd7ffca8f)

![image](https://github.com/user-attachments/assets/4f992800-8d6c-4197-bfc1-23de00357383)

![image](https://github.com/user-attachments/assets/4268deeb-6649-4df7-9550-f66f9b647d82)

## Example 2 – Roulette Wheel Selection

![image](https://github.com/user-attachments/assets/f23fc01c-cc16-4bec-ab33-db986296acc8)

![image](https://github.com/user-attachments/assets/6b942425-44eb-4fc8-8cbd-74c9851840b7)

![image](https://github.com/user-attachments/assets/975eb5ae-e54b-43ce-9a08-75eb049144a3)

![image](https://github.com/user-attachments/assets/e464ca67-4b48-4e67-80c6-20c8d8817556)

![image](https://github.com/user-attachments/assets/08cb514c-f6a7-42cc-b003-60f42cc4b604)



