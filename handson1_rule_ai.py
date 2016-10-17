import os
import gym
from agents.rule_defender import RuleDefender


def main(episode_count):
    env = gym.make("Pong-v0")
    agent = RuleDefender(action_up=2, action_down=3, action_stop=0)

    for i in range(episode_count):
        observation = env.reset()
        done = False
        score = 0

        while not done:
            env.render()
            action = agent.act(observation)
            next_observation, reward, done, info = env.step(action)

            observation = next_observation
            score += reward

            if done:
                print("Episode {} is end. score={}".format(i, score))


if __name__ == "__main__":
    main(episode_count=2)
