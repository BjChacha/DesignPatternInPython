import numpy as np
from Strategy import Strategy
from Hand import Hand


class ProbStrategy(Strategy):

    def __init__(self, seed):
        self._history = [[1 for _ in range(3)] for _ in range(3)]
        self._prev_hand_no = None
        self._curr_hand_no = None
        self._random = np.random.default_rng(seed)

    def next_hand(self):
        self._prev_hand_no = self._curr_hand_no
        if self._curr_hand_no != None:
            p_sum = sum(self._history[self._prev_hand_no])
            p = [item / p_sum for item in self._history[self._prev_hand_no]]
            self._curr_hand_no = self._random.choice(range(3), p=p)
        else:
            self._curr_hand_no = self._random.integers(0, 3)
        return Hand.get_hand(self._curr_hand_no)

    def study(self, won):
        if won and self._prev_hand_no != None:
            self._history[self._prev_hand_no][self._curr_hand_no] += 1
