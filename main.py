import runSim
from robotIndividual import RobotIndividual

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

# use the new  subclassed RobotIndividual to generate population
toolbox.register("population", tools.initRepeat, list, creator.Individual)

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
pop, log, hof = main()


# code to test various functions
# p = runSim.getRobotPosition(nsecs=5)
# print("position: ", p)
# r = RobotIndividual()
# RobotIndividual.mutate(r, 0.5)
# r.evaluate()
# print("ok")
