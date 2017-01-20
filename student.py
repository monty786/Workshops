__author__ = 'jc437351'


from person import*
class Student(Person):
    def __init__(self,name,age,id):
        super().__init__(name,age)
        self.id = id
    def get_id(self):
        return self.id
    def set_id(self,new_id):
        self.id = new_id
    def info(self):
        super().info()
        print("ID:",self.id)
    def __str__(self):
        return super().__str__()+' '+self.id

s = Student("Monty",26,"jc437351")
print("My name is:",s.get_name())
print("My age is:",s.get_age())
print("My id is:",s.get_id())
