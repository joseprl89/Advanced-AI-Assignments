import random 
from data import numberOfContainers,containerSize,packages
from pyevolve.G1DList import G1DList
from pyevolve import Crossovers
from pyevolve.GSimpleGA import GSimpleGA
from pyevolve.Mutators import G1DListMutatorSwap

# The fitness function, that identifies how correct a genome is.
# Returns the weight that is added in the containers, since pyevolve tries
# to maximize the value of the fitness function
def fitnessFunction(data):
    containerCount = 0
    includedInPackages = 0
    weightInCurrentContainer = 0
    
    # iterate over the index and value. 
    for packageWeight in data:
        # Ignore packages bigger than the container
        if (packageWeight > containerSize):
            continue
        
        # If the package doesn't fit in the container, go to next container
        if ( weightInCurrentContainer + packageWeight > containerSize):
            containerCount = containerCount + 1
            weightInCurrentContainer = 0
            
        # If the container count is not passed, increase the current container weight and 
        # the weight included in packages. 
        if containerCount < numberOfContainers:
            includedInPackages += packageWeight
            weightInCurrentContainer += packageWeight

    # The closer to 0 the higher the fitness will be. 1 would be an ideal solution.
    return includedInPackages

print ( fitnessFunction([120, 80, 20, 35, 60, 85, 90, 110, 30, 70, 100, 130, 25, 45, 40, 10]) )

def nonRepeatInitializer(genome, **args): 
    genome.clearList() 
    random.shuffle(packages) 
    [genome.append(i) for i in packages]

genome = G1DList(len(packages))
genome.evaluator.set(fitnessFunction)
genome.initializator.set(nonRepeatInitializer)
genome.mutator.set(G1DListMutatorSwap)
genome.crossover.set(Crossovers.G1DListCrossoverEdge)
ga = GSimpleGA(genome)
ga.setGenerations(200)
ga.setCrossoverRate(1.0)
ga.setMutationRate(0.03)
ga.setPopulationSize(100)

# Do the evolution, with stats dump
# frequency of 10 generations
ga.evolve(freq_stats=20)

bestIndividual =  ga.bestIndividual()

# Best individual
print(bestIndividual)
print(fitnessFunction(bestIndividual))
