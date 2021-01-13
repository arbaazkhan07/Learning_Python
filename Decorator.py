"""def decorator_function(name_function):
    def func():
        print("Before calling 'name' function")
        name_function()
        print("After calling 'name' function")

    return func


@decorator_function
def name():
    print('Arbaaz khan')


# or

# name = decorator_function(name)

name()"""

#################

# @property

'''class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f'{self.fname}.{self.lname}@gmail.com'

    def explain(self):
        return f'The emploee name is {self.fname} {self.lname}'

    @property
    def email(self):
        return f'{self.fname}.{self.lname}@gmail.com'


ak = Employee('Arbaaz', 'khan')
print(ak.explain())
print(ak.email)  # not email()
ak.fname = 'arbaaz'
print(ak.email)  # not email()'''

# setters

'''class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f'{self.fname}.{self.lname}@gmail.com'

    def explain(self):
        return f'The emploee name is {self.fname} {self.lname}'

    @property
    def email(self):
        return f'{self.fname}.{self.lname}@gmail.com'

    @email.setter
    def email(self, string):
        print('Setting now...')
        names = string.split('@')[0]
        self.fname = names.split('.')[0]
        self.lname = names.split('.')[1]


ak = Employee('Arbaaz', 'khan')
print(ak.explain())
print(ak.email)  # not email()
ak.fname = 'arbaaz'
print(ak.email)  # not email()
ak.email = 'ak.ak@gmail.com'
print(ak.fname)  # ak
print(ak.lname)  # ak
print(ak.email)  # ak.ak@gmail.com'''


# deleter

class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f'{self.fname}.{self.lname}@gmail.com'

    def explain(self):
        return f'The emploee name is {self.fname} {self.lname}'

    @property
    def email(self):
        if self.fname is None and self.lname is None:
            return 'Email is not set...'
        return f'{self.fname}.{self.lname}@gmail.com'

    @email.setter
    def email(self, string):
        print('Setting now...')
        names = string.split('@')[0]
        self.fname = names.split('.')[0]
        self.lname = names.split('.')[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


ak = Employee('Arbaaz', 'khan')
print(ak.explain())
print(ak.email)  # not email()
ak.fname = 'arbaaz'
print(ak.email)  # not email()
ak.email = 'ak.ak@gmail.com'
print(ak.fname)  # ak
print(ak.lname)  # ak
print(ak.email)  # ak.ak@gmail.com
del ak.email
print(ak.email)
