from robotIndividual import RobotIndividual
from funcsForEvaluation import getRobotPosition

import array
import random

import numpy

from deap import algorithms
from deap import base
from deap import creator
from deap import tools

# define fitness as required by framework
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
# this subclasses RobotIndividual, adding a fitness attribute
creator.create("Individual", RobotIndividual, fitness=creator.FitnessMax)
toolbox = base.Toolbox()

# use the new subclassed RobotIndividual (it's now ceator.Individual) to register population() function
toolbox.register("population", tools.initRepeat, list, creator.Individual)

# tell framework what to use as evolution operators
toolbox.register("evaluate", RobotIndividual.evaluate)
toolbox.register("mutate", RobotIndividual.mutate, prob=0.5)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():    
    pop = toolbox.population(n=10)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("max", numpy.max)
    
    # set cxpb (crossover probability) to 0 to avoid crossover for now
    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.0, mutpb=0.5, ngen=4, 
                                   stats=stats, halloffame=hof, verbose=True)
    
    return pop, log, hof

# pop is our final generation, log stores statistics, and hof 
# contains the best individuals of all time
# pop, log, hof = main()


# code to test various functions
r = RobotIndividual()
r.evaluate()
print("ok")
