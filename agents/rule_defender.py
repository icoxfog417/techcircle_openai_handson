import numpy as np


class RuleDefender():

    def __init__(self, action_up, action_down, action_stop):
        self.actions = (action_up, action_down, action_stop)
        self.action_up = action_up
        self.action_down = action_down
        self.action_stop = action_stop
        self._area_size = 80
        self._interval = 30
        self._plan = []
    
    def act(self, observation):
        if len(self._plan) == 0:
            self._plan += [self.action_up] * self._interval  # up
            self._plan += [self.action_down] * (self._interval * 2)  # back to center & down
            self._plan += [self.action_up] * self._interval  # back to center
        
        return self._plan.pop(0)
    
    def observation_to_state(self, observation):
        """
        detect player, enemy and ball position
        """
        player = []
        enemy = []
        ball = []

        background = observation[1][1]  # take background color
        area = observation[35:194]  # cut game area
        for c in background:
            area[area == c] = 0  # drop the background
        
        found = False
        for r in range(area.shape[0]):
            for c in range(area.shape[1]):
                if area[r][c][0] == 0:
                    continue
                if area[r][c][1] == 186:
                    if len(player) == 0:
                        player = (r, c)
                elif area[r][c][0] == 213:
                    if len(enemy) == 0:
                        enemy = (r, c)
                elif area[r][c][0] > 230:
                    if len(ball) == 0:
                        ball = (r, c)

                if len(player) > 0 and len(enemy) > 0 and len(ball) > 0:
                    found = True
                    break
            if found:
                break
        
        #print("player:{} enemy:{} ball:{}".format(player, enemy, ball))

        return player, enemy, ball
