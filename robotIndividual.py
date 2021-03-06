import random
import numpy as np
import csv
from funcsForEvaluation import getRobotPosition

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


class RobotIndividual:
    def __init__(self):
        # first 5 are for the organs.
        organs = [ [random.random()*10 for _ in range(3)] for _ in range(5) ]

        self.points = np.array([[5, 5, 5]])
        for _ in range(300):
            self.points = np.append(
                self.points, 
                [ 
                    [   
                        np.random.normal(loc=5, scale=2), 
                        np.random.normal(loc=5, scale=2), 
                        np.random.normal(loc=5, scale=2)
                    ]
                ],
                axis=0
            )

        ax.scatter(self.points[:, 0], self.points[:, 1], self.points[:, 2])
        plt.show()
        # z is vertical
        # self.points = organs + [ 
        #     [0, 0, 0],
        #     [2, 0, 0],
        #     [4, 0, 0],
        #     [6, 0, 0],

        #     # [0, 0, 10],
        #     # [0, 10, 10],
        #     # [10, 0, 10],
        #     # [10, 10, 10],
        # ]
        # self.points = organs + [[x, 0, 0] for x in np.linspace(0, 10, 5)]


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
        ''' writes the points to a csv file, runs sim for 1 sec, returns distance
            from origin as fitness'''

        # adjust path to your vrep installation
        with open('../V-REP_PRO_EDU_V3_5_0_Linux/Coordinates.csv', 'w') as f:
            writer = csv.writer(f, delimiter=",")
            print("points: ", self.points)
            writer.writerows(self.points)
        
        pos = getRobotPosition(nsecs=1000)
            
        return np.linalg.norm(self.points),

