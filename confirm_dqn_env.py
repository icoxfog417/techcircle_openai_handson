from collections import deque
import gym
import numpy as np
from PIL import Image
from chainer import Chain
import chainer.functions as F
from chainer import Variable


class ChainerAgent(Chain):

    def __init__(self, action, other_action, size, epsilon=0.05, hidden=200):
        self.action = action
        self.other_action = other_action
        self.width = size * size
        self.epsilon = epsilon
        self.hidden = hidden
        super(ChainerAgent, self).__init__(
            l1=F.Linear(self.width, self.hidden, wscale=np.sqrt(2)),
            l2=F.Linear(self.hidden, 1, wscale=np.sqrt(2)),
        )
    
    def __call__(self, state):
        s = Variable(np.array([state]))
        h = F.relu(self.l1(s))
        v = self.l2(h)
        p = F.sigmoid(v)
        return p.data[0][0], h.data[-1]

    def act(self, state):
        if np.random.uniform() < self.epsilon:
            action = self.action if np.random.randint(2) == 0 else self.other_action
        else:
            prob, hidden = self(state)
            action = self.action if np.random.uniform() < prob else self.other_action

        return action


def main(episode_count):
    env = gym.make("Pong-v0")
    size = 80
    frame_merge = 4
    agent = ChainerAgent(2, 3, size)

    for i in range(episode_count):
        observation = env.reset()
        done = False
        points = 0
        states = deque(maxlen=4)

        while not done:
            env.render()
            state = cut_play_area(observation, size)
            states.append(state)
            if len(states) > 4:
                state = np.max(states, axis=0)
            action = agent.act(np.array(state))
            next_observation, reward, done, info = env.step(action)
            points += reward

            if done:
                print("Episode finished. get {} points".format(points))

            observation = next_observation


def cut_play_area(observation, size):
    background = observation[1][1]
    area = observation[35:194]
    for c in background:
        area[area == c] = 0
    area[area != 0] = 1
    area = area[:,:,0]
    im = Image.fromarray(area)
    resized = im.resize((size, size))
    array = np.array(resized, dtype=np.float32).flatten()
    return array


if __name__ == "__main__":
    main(episode_count=2)
