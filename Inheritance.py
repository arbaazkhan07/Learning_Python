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

# Singal inheritence

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

'''class Khan_Parent:
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
kc.printName()'''

# Multiple Inheritance

'''class Employee:
    def __init__(self, name, salary, roll):
        self.name = name
        self.salary = salary
        self.roll = roll

    def print_emp_details(self):
        print(f'My name is {self.name} \nsalary: {self.salary} \nroll: {self.roll}')


class Player:
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def print_game_details(self):
        print(f'My name is {self.name} \ngame: {self.game}')


class CoolProgrammer(Employee, Player):
    language = ['Python', 'Java', 'C#']

    def printlang(self):
        print(f'Languages: {self.language}')


# Girish = Employee('Girish', 45000, 'Instructor')
# Girish.print_emp_details()
#
# Naveed = Player('Naveed', ['Cricket', 'Hoccky'])
# Naveed.print_game_details()

Arbaaz = CoolProgrammer('Arbaaz khan', 000, 'Student')
Arbaaz.print_emp_details()
Arbaaz.printlang()


# Arbaaz.print_game_details() ----> ERROR'''


# Multi Level Inheritance

class Addition:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.res = 0

    def add_result(self):
        self.res = self.num1 + self.num2
        print('Addition:', self.res)


class Substraction(Addition):
    def sub_result(self):
        self.res = self.num1 - self.num2
        print('Substraction:', self.res)


class Multiplication(Substraction):
    def mul_result(self):
        self.res = self.num1 * self.num2
        print('Multiplication:', self.res)


class Division(Multiplication):
    def div_result(self):
        self.res = self.num1 / self.num2
        print('Division:', self.res)


all_in_one = Division(12, 21)

all_in_one.add_result()
all_in_one.sub_result()
all_in_one.mul_result()
all_in_one.div_result()
