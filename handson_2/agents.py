import random
import numpy as np


class Agent():

    def __init__(self):
        self.reward = 0
    
    def act(self, observation):
        raise Exception("Agent have to implements act function.")

    def init(self):
        self.reward = 0


class RandomAgent(Agent):
    """
    Agent that behaves randomly.
    """

    def __init__(self, action_n):
        super().__init__()
        self.actions = list(range(action_n))
        self.reward = 0
    
    def act(self, observation):
        action = random.choice(self.actions)
        return action
    

class FunFunAgent(Agent):
    """
    Agent that behaves up side down.
    """

    def __init__(self, action_up, action_down, action_stop, interval=30):
        super().__init__()
        self.action_up = action_up
        self.action_down = action_down
        self.action_stop = action_stop
        self._interval = interval
        self._plan = []
    
    def act(self, observation):
        if len(self._plan) == 0:
            self._plan += [self.action_up] * self._interval  # up
            self._plan += [self.action_down] * (self._interval * 2)  # back to center & down
            self._plan += [self.action_up] * self._interval  # back to center
        
        return self._plan.pop(0)


class TrackAgent(Agent):
    """
    Agent that tracks ball move.
    """

    def __init__(self, action_up, action_down, action_stop):
        super().__init__()
        self.action_up = action_up
        self.action_down = action_down
        self.action_stop = action_stop
        self._past_action = self.action_stop
    
    def act(self, observation):
        player, enemy, ball = self.observation_to_state(observation)
        action = self._past_action
        if len(player) == len(ball) == 2:
            if player[0] < ball[0]:
                action = self.action_down
            else:
                action = self.action_up
            self._past_action = action

        return action

    def observation_to_state(self, observation):
        """
        detect player, enemy and ball position
        position has 2 elements, it express row and column (y and x)
        """
        player_color = [92, 186, 92]
        enemy_color = [213, 130, 74]
        ball_color = [236, 236, 236]

        area = observation[35:194]  # cut game area

        player = self.search_position(area, player_color)
        enemy = self.search_position(area, enemy_color)
        ball = self.search_position(area, ball_color)

        #print("player:{} enemy:{} ball:{}".format(player, enemy, ball))
        return player, enemy, ball

    def search_position(self, area, color):
        position = []
        index = np.where(area == color)
        if len(index[0]) > 0:
            position = [index[0][0], index[1][0]]
        return position
