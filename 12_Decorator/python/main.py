from StringDisplay import StringDisplay
from SideBorder import SideBorder
from FullBorder import FullBorder

b1 = StringDisplay("Hello, World.")
b2 = SideBorder(b1, "#")
b3 = FullBorder(b2)

b1.show()
b2.show()
b3.show()

b4 = SideBorder(FullBorder(FullBorder(SideBorder(FullBorder(StringDisplay("你好，世界。")), "*"))), "/")
b4.show()