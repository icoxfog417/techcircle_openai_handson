from collections import deque
import numpy as np


class Trainer():

    def __init__(self, agent, gamma=0.95, learning_rate=0.1, learning_rate_decay=None, epsilon=0.05, epsilon_decay=None, max_step=-1):
        self.agent = agent
        self.gamma = gamma
        self.learning_rate = learning_rate
        self.learning_rate_decay = learning_rate_decay
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.max_step = max_step

    def train(self, env, episode_count, render=False):
        default_epsilon = self.agent.epsilon
        self.agent.epsilon = self.epsilon
        values = []
        steps = deque(maxlen=100)
        lr = self.learning_rate
        for i in range(episode_count):
            obs = env.reset()
            step = 0
            done = False
            while not done:
                if render:
                    env.render()

                action = self.agent.act(obs)
                next_obs, reward, done, _ = env.step(action)

                state = self.agent.q.observation_to_state(obs)
                future = 0 if done else np.max(self.agent.q.values(next_obs))
                value = self.agent.q.table[state][action]
                self.agent.q.table[state][action] += lr * (reward + self.gamma * future - value)

                obs = next_obs
                values.append(value)
                step += 1
                if self.max_step > 0 and step > self.max_step:
                    done = True
            else:
                mean = np.mean(values)
                steps.append(step)
                mean_step = np.mean(steps)
                print("Episode {}: {}steps(avg{}). epsilon={:.3f}, lr={:.3f}, mean q value={:.2f}".format(
                    i, step, mean_step, self.agent.epsilon, lr, mean)
                    )
                
                if self.epsilon_decay is not None:
                    self.agent.epsilon = self.epsilon_decay(self.agent.epsilon, i)
                if self.learning_rate_decay is not None:
                    lr = self.learning_rate_decay(lr, i)
