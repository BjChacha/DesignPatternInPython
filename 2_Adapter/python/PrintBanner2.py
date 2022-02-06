from Print import Print
from Banner import Banner

class PrintBanner2(Print):
    def __init__(self, string):
        self.banner = Banner(string)

    def print_strong(self):
        self.banner.show_with_aster()

    def print_weak(self):
        self.banner.show_with_paren()