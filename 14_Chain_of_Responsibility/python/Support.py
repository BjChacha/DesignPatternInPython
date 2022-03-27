class Support:

    def __init__(self, name):
        self._name = name
        self._next = None

    def set_next(self, next):
        self._next = next
        return next

    def support(self, trouble):
        if self.resolve(trouble):
            self.done(trouble)
        elif self._next:
            self._next.support(trouble)
        else:
            self.fail(trouble)

    def __str__(self):
        return f'[{self._name}]'

    def resolve(self, trouble):
        raise NotImplementedError
    
    def done(self, trouble):
        print(f'{trouble} is resolved by {self}.')

    def fail(self, trouble):
        print(f'{trouble} cannot be resolved.')