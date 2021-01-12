# Method Overloading

"""class Addition:
    def add(self, a=None, b=None, c=None):

        if a != None and b != None and c != None:
            r = a + b + c
        elif a != None and b != None:
            r = a + b
        else:
            r = a
        return r


a1 = Addition()
print(a1.add(23, 32, 45))
print(a1.add(23, 32,))
print(a1.add(23))"""

# Method Overriding

'''class A:
    def show(self):
        print('We are in A class..')


class B(A):
    def show(self):
        print('We are in B class..')


a = A()
b = B()
a.show()
b.show()'''

#########

'''class A:
    classvar1 = 'I am in class variable in class A.. '

    def __init__(self):
        self.var1 = "I am in instance variable 'var1' in class A"
        self.classvar1 = "I am in instance variable 'var1'  in class A"


class B(A):
    classvar2 = 'I am in class variable in class B.. '


a = A()
b = B()

print(b.classvar1)'''


#  Super()

class A:
    classvar1 = 'I am in class variable in class A.. '

    def __init__(self):
        self.var1 = "I am in instance variable 'var1' in class A"
        self.classvar1 = "I am in instance variable 'classvar1'  in class A"
        self.special = 'SPECIAL'


class B(A):
    classvar1 = 'I am in class variable in class B.. '

    def __init__(self):     # Method Overriding
        # super().__init__()
        self.var1 = "I am in instance variable 'var2' in class B"
        self.classvar1 = "I am in instance variable 'classvar2'  in class B"
        super().__init__()
        print(super().classvar1)


a = A()
b = B()

print(b.special)
print(b.var1)
print(b.classvar1)
