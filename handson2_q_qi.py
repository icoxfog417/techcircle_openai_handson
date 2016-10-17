import os
import math
import argparse
import gym
from agents.q_agent import Q, Agent, Trainer


RECORD_PATH = os.path.join(os.path.dirname(__file__), "./upload")


def main(episodes, render, monitor):
    env = gym.make("CartPole-v0") 

    q = Q(
        env.action_space.n, 
        env.observation_space, 
        bin_size=[7, 7, 7, 7],
        low_bound=[-5, -0.5, -5, -0.5], 
        high_bound=[5, 0.5, 5, 0.5]
        )
    agent = Agent(q, epsilon=0.05)

    learning_decay = lambda lr, t: 1 / (t + 1) ** 0.5
    epsilon_decay = lambda eps, t: 1 / (t + 1) ** 0.5
    trainer = Trainer(
        agent, 
        gamma=0.95,
        learning_rate=0.1, learning_rate_decay=learning_decay, 
        epsilon=1.0, epsilon_decay=epsilon_decay,
        max_step=250)

    if monitor:
        env.monitor.start(RECORD_PATH)

    trainer.train(env, episode_count=episodes, render=render)

    if monitor:
        env.monitor.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="train & run cartpole ")
    parser.add_argument("--episode", type=int, default=1000, help="episode to train")
    parser.add_argument("--render", action="store_true", help="render the screen")
    parser.add_argument("--monitor", action="store_true", help="monitor")
    parser.add_argument("--upload", type=str, default="", help="upload key to openai gym (training is not executed)")

    args = parser.parse_args()

    if args.upload:
        if os.path.isdir(RECORD_PATH):
            gym.upload(RECORD_PATH, api_key=args.upload)
    else:
        main(args.episode, args.render, args.monitor)
