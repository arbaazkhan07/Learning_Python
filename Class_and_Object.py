# simple class

"""class MyClass:
    pass"""

# Creating object

'''class MyClass:
    x = 5


mc = MyClass()
print(mc.x)'''

# The __init__ function

'''class Khan:
    def __init__(self, name, age):
        self.name = name
        self.age = age


k = Khan('Arbaaz khan', 23)
print(k.name)
print(k.age)'''

# OR

'''class Khan:
    def __init__(ak, name, age):
        ak.name = name
        ak.age = age


k = Khan('Arbaaz khan', 23)
print(k.name)
print(k.age)'''

# Object methods (functions)

'''class Khan:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def ak(self):
        print(f'My name is {self.name} and my age is {self.age}')


k = Khan('Arbaaz khan', 23)
print(k.name)
print(k.age)
k.ak()
# print(k)  <__main__.Khan object at 0x000001A6DB574A00>'''

# Modify object

'''class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print(f'Age before modified {self.age}')

    def myfunc1(self):
        print(f'Age after modified {self.age}')


mc = MyClass('Arbaaz khan', 20)
print(mc.name)
mc.myfunc()
mc.age = 23
mc.myfunc1()'''

# Delete object properties

'''class Delete:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Before(self):
        print(f'Before deleting age {self.age}')

    def After(self):
        print(f'After deleting age {self.age}')


d = Delete('Arbaaz khan', 23)
print(d.name)
d.Before()
del d.age
# d.After() --> 'Delete' object has no attribute 'age' '''


# Delete object

'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("Arbaaz khan", 23)

del p1

# print(p1) --> name 'p1' is not defined'''
