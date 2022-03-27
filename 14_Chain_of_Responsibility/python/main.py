from tokenize import Special
from Trouble import Trouble
from NotSupport import NotSupport
from LimitSupport import LimitSupport
from OddSupport import OddSupport
from SpecialSupport import SpecialSupport

def main():
    alice = NotSupport('Alice')
    bob = LimitSupport('Bob', 100)
    charlice = SpecialSupport('Charlice', 429)
    diana = LimitSupport('Diana', 200)
    elmo = OddSupport('Elmo')
    fred = LimitSupport('Fred', 300)

    alice.set_next(bob).set_next(charlice).set_next(diana).set_next(elmo).set_next(fred)
    
    for i in range(0, 500, 33):
        alice.support(Trouble(i))

if __name__ == '__main__':
    main()