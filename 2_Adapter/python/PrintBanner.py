from Print import Print
from Banner import Banner

class PrintBanner(Print, Banner):

    def print_weak(self):
        self.show_with_paren()

    def print_strong(self):
        self.show_with_aster()