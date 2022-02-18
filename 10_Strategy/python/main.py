from Player import Player
from ProbStrategy import ProbStrategy
from WinningStrategy import WinningStrategy

import sys

def main():
    if len(sys.argv) != 3:
        print(f"Usage: python main.py randomseed1 randomseed2")
        print(f"Example: python main 314, 12")
        sys.exit(0)
    
    seed1, seed2  = int(sys.argv[1]), int(sys.argv[2])
    player1 = Player("Taro", WinningStrategy(seed1))
    player2 = Player("Hana", ProbStrategy(seed2))
    
    for i in range(10000):
        next_hand1 = player1.next_hand()
        next_hand2 = player2.next_hand()
        if next_hand1.is_stronger_than(next_hand2):
            player1.win()
            player2.lose()
            print(f"round {i+1} Winner: {player1}")
        elif next_hand1.is_weaker_than(next_hand2):
            player1.lose()
            player2.win()
            print(f"round {i+1} Winner: {player2}")
        else:
            player1.even()
            player2.even()
            print("Even...")

    print("Total result:")
    print(player1)
    print(player2)


if __name__ == '__main__':
    main()