from re import T
from Triple import Triple

obj1 = Triple()
obj2 = Triple()
obj3 = Triple()
obj4 = Triple()
obj5 = Triple()

obj11 = Triple.get_instance(0)
obj22 = Triple.get_instance(1)
obj33 = Triple.get_instance(2)

print(f'{obj1 = }')
print(f'{obj2 = }')
print(f'{obj3 = }')
print(f'{obj4 = }')
print(f'{obj5 = }')

print(f'{Triple.get_instance(0) = }')
print(f'{Triple.get_instance(1) = }')
print(f'{Triple.get_instance(2) = }')