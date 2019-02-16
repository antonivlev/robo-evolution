import random

class RobotIndividual:
    def __init__(self):
        self.name = "dave"
        self.points = [ random.random()*10 for _ in range(10) ]

    def sayMyName(self):
        print(self.name)
