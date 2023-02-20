import numpy as np


class DataProcess:
    def __init__(self):
        self.loadRacetrack()
        self.loadStates()
        self.loadstateActionValue()
        self.loadPolicy()
        self.loadRewards()
        self.discount = 0.99
        self.episode = {"S": [], "A": [], "probs": [], "R": [None]}

    def loadRacetrack(self):
        self.racetrack = np.asarray([
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 2],
            [0, 1, 1, 0, 1, 1, 1, 2],
            [0, 1, 1, 0, 1, 0, 1, 2],
            [0, 1, 1, 0, 1, 1, 1, 2],
            [0, 1, 1, 1, 1, 0, 1, 2],
            [0, 1, 1, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 3, 3, 3, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ])
        self.rows = 21
        self.cols = 8

    def loadStates(self):
        self.startLine = []
        for j in range(self.cols):
            if (self.racetrack[self.rows - 1, j] == 3):
                self.startLine.append(np.array([self.rows - 1, j]))

        self.startLine = np.array(self.startLine)

        self.finishLine = []
        for i in range(self.rows):
            if (self.racetrack[i, self.cols - 1] == 2):
                self.finishLine.append(np.array([i, self.cols - 1]))

        self.finishLine = np.array(self.finishLine)
        
        self.walls = []
        for i in range(self.rows):
            for j in range(self.cols):
                if(self.racetrack[i,j] == 0):
                    self.walls.append(np.array([i,j]))
        
        self.walls = np.array(self.walls)

    def loadstateActionValue(self):
        self.q = np.full((21, 8, 6, 6, 3), 0)

    def loadPolicy(self):
        self.pi = np.full((21, 8, 6, 6, 3), 1/9)

    def loadRewards(self):
        self.rewards = np.asarray([])
