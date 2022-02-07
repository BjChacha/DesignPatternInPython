from Singleton import Singleton, Singleton2


print("Start.")
obj1 = Singleton.get_instance()
obj2 = Singleton.get_instance()
if obj1 == obj2:
    print("obj1和obj2是相同的实例。")
else:
    print("obj1和obj2是不同的实例。")

print("Start.")
obj3 = Singleton2()
obj4 = Singleton2()
if obj3 == obj4:
    print("obj3和obj4是相同的实例。")
else:
    print("obj3和obj4是不同的实例。")