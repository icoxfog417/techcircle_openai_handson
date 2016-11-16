import os
import argparse
import gym


def main(env_name, episode_count):
    env = gym.make(env_name)

    for i in range(episode_count):
        observation = env.reset()
        done = False
        score = 0

        while not done:
            env.render()
            action = env.action_space.sample()
            next_observation, reward, done, info = env.step(action)
            print(next_observation)

            observation = next_observation
            score += reward

            if done:
                print("Episode {} is end. score={}".format(i, score))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Let's Start OpenAI Gym")
    parser.add_argument("--env", type=str, help="Name of environment", default="Pong-v0")
    parser.add_argument("--episode", type=int, help="Episode Count to work", default=2)

    args = parser.parse_args()
    main(args.env, args.episode)
