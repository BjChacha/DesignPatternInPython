class AbstractDisplay:
    def open(self):
        raise NotImplementedError

    def print(self):
        raise NotImplementedError
    
    def close(self):
        raise NotImplementedError

    def display(self):
        self.open()
        for _ in range(5):
            self.print()
        self.close()