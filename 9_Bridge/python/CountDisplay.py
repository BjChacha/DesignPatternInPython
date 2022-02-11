from Display import Display

class CountDisplay(Display):

    def multi_display(self, times):
        self.open()
        for t in range(times):
            self.print()
        self.close()