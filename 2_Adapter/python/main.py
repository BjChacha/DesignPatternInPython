from PrintBanner import PrintBanner
from PrintBanner2 import PrintBanner2

print("类适配器模式：")
printer = PrintBanner("Hello")
printer.print_weak()
printer.print_strong()

print("对象适配模式：")
printer2 = PrintBanner2("Hello")
printer2.print_weak()
printer2.print_strong()