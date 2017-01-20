__author__ = 'jc437351'

from person import *

p =Person("Monty",26)
print("My name is:",p.get_name())
print("My age is:",p.get_age())
p.set_name("Manraj")
print("My name is:",p.get_name())

print(p)