import runSim
from robotIndividual import RobotIndividual, crossRobots

import array
import random

import numpy

from deap import algorithms
from deap import base
from deap import creator
from deap import tools

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", RobotIndividual, fitness=creator.FitnessMax)
toolbox = base.Toolbox()

# Structure initializers
toolbox.register("population", tools.initRepeat, list, creator.Individual)

toolbox.register("evaluate", RobotIndividual.evaluate)
# toolbox.register("mate", crossRobots)
toolbox.register("mutate", RobotIndividual.mutate, prob=0.5)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    random.seed(64)
    
    pop = toolbox.population(n=300)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)
    
    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.0, mutpb=0.5, ngen=40, 
                                   stats=stats, halloffame=hof, verbose=True)
    
    return pop, log, hof

pop, log, hof = main()

# # p = runSim.getRobotPosition(nsecs=0.05)
# # print("position: ", p)
# r = RobotIndividual()
# RobotIndividual.mutate(r, 0.5)
# print("ok")
