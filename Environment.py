from DataProcess import DataProcess
import numpy as np

class Environment:
    def __init__(self,data):
        self.data = data
        self.raceCourse = self.data.racetrack
        self.step_count = 0
        
    def reset(self):
        self.data.episode = {"S": [], "A": [], "probs": [], "R": [None]}
        self.step_count = 0
        
    def startState(self):
        """
        state[0] = row number
        state[1] = column number
        state[2] = x component of velocity
        state[2] = y component of velocity
        """
        state = np.zeros(4,dtype=int)
        state[0] = 19
        state[1] = np.random.choice(self.data.startLine[:,1])
        return state

    def nextState(self,state,action):
        newState = state.copy()
        newState[0] = state[0] - state[2]
        newState[1] = state[1] + state[3]
        newState[2] = state[2] + action[0]
        newState[3] = state[3] + action[1]
        return newState
    
    def finishLineCrossed(self,state,action):
        newState = self.nextState(state,action)
        coord,newCoords = state[:2],newState[:2]
        
        finishline = [tuple(x) for x in self.data.finishLine]
        intersect = 0

        return False
    
    def isWall(self,state,action):
        newState = self.nextState(state,action)
        coords,newCoords = state[:2],newState[:2]
        
        walls = [tuple(x) for x in self.data.walls]
        unit_vector = [(newCoords[0] - coords[0])/5,(newCoords[1] - coords[1])/5]
        if(newCoords in walls): return True
        while(int(coords[0]) != newCoords[0] and int(coords[1]) != newCoords[1]):
            coords[0] = coords[0] + unit_vector[0] + 0.5
            coords[1] = coords[1] + unit_vector[1] + 0.5
            if((int(coords[0]),int(coords[1])) in walls):
                return True
            
        return False
    
    def isOutOfTrack(self,state,action):
        newState = self.nextState(state,action)
        coords,newCoords = state[:2],newState[:2]
        
        if(newCoords[0] < 0 or newCoords[0] >= self.data.rows or newCoords[1] < 0 or newCoords[1] >= self.data.cols):
            return True
        
        else:
            return self.data.racetrack[tuple(newCoords)] == -1
        
        
    def step(self):
        
                 
    
            
            