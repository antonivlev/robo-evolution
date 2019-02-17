import random

class RobotIndividual:
    def __init__(self):
        self.points = [ random.random()*10 for _ in range(10) ]

    def mutate(self, prob):
        mutatePoint = lambda x: x+1 if random.random() <= 0.5 else x-1

        self.points = [
            mutatePoint(point) if random.random()<=prob else point 
            for point in self.points
        ]

        return self,
    
    def evaluate(self):
        return sum(self.points),


def crossRobots(robot1, robot2):
    return robot1, robot2
