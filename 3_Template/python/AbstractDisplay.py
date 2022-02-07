class AbstractDisplay:
    def _open(self):
        raise NotImplementedError

    def _print(self):
        raise NotImplementedError
    
    def _close(self):
        raise NotImplementedError

    def display(self):
        self._open()
        for _ in range(5):
            self._print()
        self._close()