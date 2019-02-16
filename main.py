import runSim
from robotIndividual import RobotIndividual

from deap import algorithms
from deap import base
from deap import creator
from deap import tools

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", RobotIndividual, fitness=creator.FitnessMax)
toolbox = base.Toolbox()

# Structure initializers
toolbox.register("population", tools.initRepeat, list, creator.Individual)
pop = toolbox.population(n=300)

# p = runSim.getRobotPosition(nsecs=0.05)
# print("position: ", p)
r = RobotIndividual()
r.sayMyName()
print("ok")
