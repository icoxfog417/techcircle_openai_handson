import numpy as np
from chainer import Chain
import chainer.functions as F
from chainer import Variable


class ChoiceAgent(Chain):

    def __init__(self, action, other_action, size, epsilon=0.05, hidden=200):
        self.action = action
        self.other_action = other_action
        self.width = size * size
        self.epsilon = epsilon
        self.hidden = hidden
        super(ChoiceAgent, self).__init__(
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
