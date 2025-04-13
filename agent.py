import numpy as np

ACTIONS = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}


class Agent(object):
    # NOTE: alpha is the learning rate
    # NOTE: random_factor is the % chance of choosing the action that maximizes reward, as opposed to taking a random action
    def __init__(self, states, alpha=.15,
                 random_factor=.20):  # 80% explore, 20% exploit are default values if not set in main()
        self.state_history = [((0, 0), 0)]  # state, reward
        self.alpha = alpha
        print("INIT: random_factor = " + str(random_factor))
        self.randomFactor = random_factor
        self.G = {}
        self.init_reward(states)

    def init_reward(self, states):
        for i, row in enumerate(states):
            for j, col in enumerate(row):
                self.G[(j, i)] = np.random.uniform(low=1.0, high=0.1)

    def choose_action(self, state, allowedMoves):
        maxG = -10e15
        next_move = None
        randomN = np.random.random()
        if randomN < self.randomFactor:
            # if random number below random factor, choose random action
            next_move = np.random.choice(allowedMoves)
        else:
            # if exploiting, gather all possible actions and choose one with the highest G (reward)
            for action in allowedMoves:
                new_state = tuple([sum(x) for x in zip(state, ACTIONS[action])])
                if self.G[new_state] >= maxG:
                    next_move = action
                    maxG = self.G[new_state]

        return next_move

    def update_state_history(self, state, reward):
        self.state_history.append((state, reward))

    def learn(self):
        target = 0

        for prev, reward in reversed(self.state_history):
            self.G[prev] = self.G[prev] + self.alpha * (target - self.G[prev])
            target += reward

        self.state_history = []

        self.randomFactor -= 10e-5  # decrease random factor each episode of play
