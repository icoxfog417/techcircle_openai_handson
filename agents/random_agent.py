import random


class RandomAgent():

    def __init__(self, action_n):
        self.actions = list(range(action_n))
    
    def act(self, observation):
        action = random.choice(self.actions)
        return action
