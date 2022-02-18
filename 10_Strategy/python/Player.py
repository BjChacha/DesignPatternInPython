from Hand import Hand

class Player:

    def __init__(self, name, strategy):
        self._name = name
        self._strategy = strategy
        self._game_count = 0
        self._win_count = 0
        self._lose_count = 0

    def next_hand(self):
        return self._strategy.next_hand()

    def win(self):
        self._strategy.study(True)
        self._game_count += 1
        self._win_count += 1

    def lose(self):
        self._strategy.study(False)
        self._game_count += 1
        self._lose_count += 1

    def even(self):
        self._game_count += 1

    def __str__(self):
        return f"[{self._name}:{self._game_count} games, {self._win_count} win, {self._lose_count} lose]"