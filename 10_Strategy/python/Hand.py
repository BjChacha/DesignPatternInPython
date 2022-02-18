
class Hand:

    def __init__(self, handvalue):
        self._handvalue = handvalue

    @classmethod
    def get_hand(cls, handvalue):
        HANDVALUE_GUU = 0
        HANDVALUE_CHO = 1
        HANDVALUE_PAA = 2
        
        if not hasattr(cls, '_hand'):
            cls._hand = [
                Hand(HANDVALUE_GUU),
                Hand(HANDVALUE_CHO),
                Hand(HANDVALUE_PAA)
            ]
        return cls._hand[handvalue]

    def is_stronger_than(self, hand):
        return self._fight(hand) == 1
    
    def is_weaker_than(self, hand):
        return self._fight(hand) == -1

    def _fight(self, hand): 
        if self._handvalue == hand._handvalue:
            return 0
        elif (self._handvalue + 1) % 3 == hand._handvalue:
            return 1
        else:
            return -1
    
    def __repr__(self):
        name = ['石头', '剪刀', '布']
        return name[self._handvalue]
        