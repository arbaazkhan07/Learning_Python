"""def myfun():
    print()
    print('Hello! My name is Khan')
    print()


myfun()


def addition():
    print(num, '+', num1, '=', num + num1)


num = int(input('Enter 1st number :\n'))
num1 = int(input('Enter 2st number :\n'))
addition()"""

# Arguments

'''def multi(x, y):  # Parameters
    print()
    z = x * y
    return z


print('Multiplication of 5 and 5 is:', multi(5, 5))  # Arguments


def subs(a, b):
    print()
    c = a - b
    return c


d = subs(4, 2)
print('Substrction:', d)'''

# DOCSTRING
'''def division(a, b):
    """Division of two numbers"""
    print()
    c = a / b
    return c


e = division(15, 5)
print(division.__doc__)
print('Division:', e)'''

# Local And Global variables

var1 = 23  # Global variable

'''def ak():
    var1 = 10  # Local variable
    print(var1)


ak()
print(var1)'''

# Changing global variable in a function

'''var2 = 45

def ak1():
    global var2
    var2 = 80
    print(var2)

ak1()
print(var2)'''

var3 = 0


def ak2():
    var3 = 12

    def ak3():
        global var3
        var3 = 34
        print(var3)  # 34

    ak3()
    print(var3)  # 12


ak2()
print(var3)  # 34 (Global)
