# Parent class

"""class Khan:
    def __init__(self, fname, lname, age):
        self.firstName = fname
        self.lastName = lname
        self.age = age

    def printName(self):
        print(f'My name is {self.firstName} {self.lastName} and my age is {self.age}')


k = Khan('Arbaaz', 'khan', 23)
k.printName()"""

# Child class

'''class Khan:
    def __init__(self, fname, lname, age):
        self.firstName = fname
        self.lastName = lname
        self.age = age

    def printName(self):
        print(f'My name is {self.firstName} {self.lastName} and my age is {self.age}')


class Khan_child(Khan):
    pass


kc = Khan_child('Arbaaz', 'khan', 23)
kc.printName()'''


# __init__

class Khan_Parent:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def printName(self):
        print(f'My name is {self.fname} {self.lname} and my age is {self.age}')


class Khan_Child(Khan_Parent):
    def __init__(self, fname, lname, age):
        Khan_Parent.__init__(self, fname, lname, age)


kc = Khan_Child('Arbaaz', 'khan', 23)
kc.printName()
