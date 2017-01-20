__author__ = 'jc437351'


class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_name(self,new_name):
        self.name = new_name
    def set_age(self,new_age):
        self.age = new_age
    def info(self):
        print("Name:",self.name)
        print("Age:",self.age)
    def __str__(self):
           return self.name+' '+str(self.age)


p =Person("Monty",26)
print("My name is:",p.get_name())
print("My age is:",p.get_age())
p.set_name("Manraj")
print("My name is:",p.get_name())