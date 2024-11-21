class myClass:
    x=5
p1=myClass() #Create Object
print(p1.x)

"""__init__ Method"""

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person("Rahim",26)
print(p1.name)
print(p1.age)
        
"""Add __str__ Method"""

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name} {self.age}"
p1=Person("Rahim",26)
print(p1)

"""Add myfunc() Method in class"""
print("\nObject Call")
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name} {self.age}"

    def myfunc(self):
        return f"i'm {self.name} and im {self.age} years old"
p1=Person("Halim",26)
print(p1.myfunc())
print(p1)
