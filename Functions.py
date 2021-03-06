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

'''var1 = 23  # Global variable

def ak():
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
print(var2)

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
print(var3)  # 34 (Global)'''

# Iterative And Recursipn

# Iterative - Factorial

'''def iterative_factorial(ifn):
    fact = 1
    for i in range(ifn):
        fact = fact * (i + 1)
    return fact


fnum = int(input("Enter a number to find it's Factorial: "))
print("The Factorial of", fnum, "is:(Iterative)", iterative_factorial(fnum))


# Recursion - Factorial

def recursion_factorial(rfn):
    if rfn == 0:
        return 0
    elif rfn == 1:
        return 1
    else:
        return rfn * recursion_factorial(rfn - 1)


f1num = int(input("Enter a number to find it's Factorial: "))
print("The Factorial of", f1num, "is:(Recursion)", recursion_factorial(f1num))'''

# Iterative - Fibonacci

'''def iterative_fibonacci(ifbn):
    first = 0
    second = 1
    if ifbn == 0:
        print("Plz enter above 0..")
    elif ifbn == 1:
        print(first)
    else:
        print(first, second, end=" ")
        for i in range(ifbn - 2):
            fibo = first + second
            print(fibo, end=" ")
            first = second
            second = fibo


f2num = int(input("Enter a how many Fibonacci numbers you want?\n"))
iterative_fibonacci(f2num)'''

# How to pass Parameters

'''def up(x):
    print(id(x))
    x = 3
    print(id(x))
    print(x)


a = 10
print(id(a))
up(a)
print(a)'''

# Types of Parameters

'''def add(x, y):  # Formal Arguments/Parameters
    z = x + y
    print(z)


add(5, 6)  # Actual Parameters


# Typs of Actual Parameters

# Position

def person(name, age):
    print(name, age)


person("Arbaaz khan", 23)


# Keyword

def person1(name, age):
    print(name, age)


person1(age=23, name="Arbaaz khan")


# Default

def person2(name, age=23):
    print(name, age)


person2("Arbaaz khan")


# Veriable Length

def add1(x, *y):  # 'x' is now 5 AND '*y' is a tuple of (6, 7, 8, 9)

    print(x)
    print(y)
    for i in y:
        x = x + i
    print(x)


add1(5, 6, 7, 8, 9)


# OR

def add2(*y):  # '*y' is a tuple of (6, 7, 8, 9)
    x = 0
    print(y)
    for i in y:
        x = x + i
    print(x)


add2(6, 7, 8, 9)


#  Keyworded Variable Length

def person3(name='Arbaaz khan', **details):
    print('Name :', name)
    # print(details)
    for i, j in details.items():
        print(i, ':', j)


person3(Age=23, Address='Belgaum', Phone_no=9876543210)'''


# Pass List to a Function


'''def pass_list_fun(lst):
    even = 0
    odd = 0

    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


lst = [75, 49, 88, 46, 72, 89, 46, 87, 28, 65, 87, 98, 74, 65, 83, 74, 56, 77, 84, 35, 79, 85, 87, 29]
even, odd = pass_list_fun(lst)
print(f'Even numbers: {even} and Odd numbers: {odd}')'''
