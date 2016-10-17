import random
import copy
from collections import defaultdict
from collections import deque
from collections import namedtuple
import numpy as np


class Q():

    def __init__(self, n_actions, observation_space, bin_size, low_bound=None, high_bound=None, initial_mean=0.0, initial_std=0.0):
        self.n_actions = n_actions
        self._observation_dimension = 1
        for d in observation_space.shape:
            self._observation_dimension *= d

        self._bin_sizes = bin_size if isinstance(bin_size, list) else [bin_size] * self._observation_dimension
        self._dimension_bins = []
        for i, low, high in self._low_high_iter(observation_space, low_bound, high_bound):
            b_size = self._bin_sizes[i]
            bins = self._make_bins(low, high, b_size)
            self._dimension_bins.append(bins)

        # if we encounter the new observation, we initialize action evaluations
        self.table = defaultdict(lambda: initial_std * np.random.randn(self.n_actions) + initial_mean)
    
    @classmethod
    def _make_bins(cls, low, high, bin_size):
        bins = np.arange(low, high, (float(high) - float(low)) / (bin_size - 2))  # exclude both ends
        if min(bins) < 0 and 0 not in bins:
            bins = np.sort(np.append(bins, [0]))  # 0 centric bins
        return bins
    
    @classmethod
    def _low_high_iter(cls, observation_space, low_bound, high_bound):
        lows = observation_space.low
        highs = observation_space.high
        for i in range(len(lows)):
            low = lows[i]
            if low_bound is not None:
                _low_bound = low_bound if not isinstance(low_bound, list) else low_bound[i]
                low = low if _low_bound is None else max(low, _low_bound)
            
            high = highs[i]
            if high_bound is not None:
                _high_bound = high_bound if not isinstance(high_bound, list) else high_bound[i]
                high = high if _high_bound is None else min(high, _high_bound)
            
            yield i, low, high

    def observation_to_state(self, observation):
        state = 0
        # caution: bin_size over 10 will not work accurately
        unit = max(self._bin_sizes)
        for d, o in enumerate(observation.flatten()):
            state = state + np.digitize(o, self._dimension_bins[d]) * pow(unit, d)  # bin_size numeral system
        return state
    
    def values(self, observation):
        state = self.observation_to_state(observation)
        return self.table[state]


class Agent():

    def __init__(self, q, epsilon=0.05):
        self.q = q
        self.epsilon = epsilon
    
    def act(self, observation):
        action = -1
        if np.random.random() < self.epsilon:
            action = np.random.choice(self.q.n_actions)
        else:
            action = np.argmax(self.q.values(observation))
        
        return action


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
