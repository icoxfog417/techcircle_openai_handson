import random
import numpy as np


class Agent():

    def __init__(self, q, epsilon=0.05):
        self.q = q
        self.epsilon = epsilon
    
    def act(self, observation):
        # your code here
