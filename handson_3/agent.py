import random
import numpy as np


class Agent():

    def __init__(self, q, epsilon=0.05):
        self.q = q
        self.epsilon = epsilon
    
    def act(self, observation):
        # your code here
        action = -1
        if np.random.random() < self.epsilon:
            action = np.random.choice(self.q.n_actions)
        else:
            action = np.argmax(self.q.values(observation))
        
        return action
