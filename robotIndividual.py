import random
import numpy as np
import csv
import runSim

class RobotIndividual:
    def __init__(self):
        # Right now a robot is a list of 50 coordinates, first 5 are for the organs.
        # Eventally the idea is to have the gaussians initiated here,
        # and generate the actual points only on evaluation of the individual
        self.points = [ 
            [random.random()*10, random.random()*10, random.random()*10]  
            for _ in range(50) 
        ]

    def mutate(self, prob):
        # will define mutation for our gaussian centers/widths here
        def mutatePoint(point):
            '''nudge a coordinte in a random direction with small magnitude'''
            nudge = lambda x: x + random.random() - 0.5
            return [
                nudge(point[0]), 
                nudge(point[1]), 
                nudge(point[2])
            ]

        self.points = [
            mutatePoint(point) if random.random()<=prob else point 
            for point in self.points
        ]

        return self,
    
    def evaluate(self):
        # adjust path to your vrep installation
        with open('../V-REP_PRO_EDU_V3_5_0_Linux/Coordinates.csv', 'w') as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerows(self.points)

        pos = runSim.getRobotPosition(1)
        return np.linalg.norm(self.points),

