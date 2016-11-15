import os
import argparse
import gym


def main(env_name, episode_count):
    # your code here


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Let's Start OpenAI Gym")
    parser.add_argument("--env", type=str, help="Name of environment", default="Pong-v0")
    parser.add_argument("--episode", type=int, help="Episode Count to work", default=2)

    args = parser.parse_args()
    main(args.env, args.episode)
