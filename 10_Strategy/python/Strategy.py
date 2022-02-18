class Strategy:

    def next_hand(self):
        raise NotImplementedError

    def study(self, win):
        raise NotImplementedError
