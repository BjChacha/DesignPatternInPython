import numpy as np

from Hand import Hand
from Strategy import Strategy


class WinningStrategy(Strategy):

    def __init__(self, seed):
        self._won = False;
        self._prev_hand = None;
        self._random = np.random.default_rng(seed)

    def next_hand(self):
        if not self._won:
            self._prev_hand = Hand.get_hand(self._random.integers(0, 3))
        return self._prev_hand

    def study(self, win):
        self._won = win
