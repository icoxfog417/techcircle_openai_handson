from collections import deque
import gym
import numpy as np
from PIL import Image
from agents.choice_agent import ChoiceAgent


def main(episode_count):
    env = gym.make("Pong-v0")
    size = 80
    frame_merge = 4
    agent = ChoiceAgent(2, 3, size)

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
    main(episode_count=20)
