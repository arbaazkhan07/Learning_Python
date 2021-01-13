class Employee:
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
# print(ak.explain())
# print(ak.email)  # not email()
# ak.fname = 'arbaaz'
# print(ak.email)  # not email()
# ak.email = 'ak.ak@gmail.com'
# print(ak.fname)  # ak
# print(ak.lname)  # ak
# print(ak.email)  # ak.ak@gmail.com

print(type(ak))  # <class '__main__.Employee'>
print(id(ak))
print(type('My name is KHAN'))  # <class 'str'>
print(id('My name is KHAN'))
print(dir('My name is KHAN'))  # ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', # '__getnewargs__', '__gt__', '__hash__',
# '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs',
# 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit',
# 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust',
# 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
# 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
print(dir(ak))  # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__', '__weakref__', 'email', 'explain', 'fname', 'lname']

import inspect

print(inspect.getmembers(ak))  # [('__class__', <class '__main__.Employee'>),
# ('__delattr__', <method-wrapper '__delattr__' of Employee object at 0x0000020F61EF5520>),
# ('__dict__', {'fname': 'Arbaaz', 'lname': 'khan'}),
# ('__dir__', <built-in method __dir__ of Employee object at 0x0000020F61EF5520>),
# ('__doc__', None), ('__eq__', <method-wrapper '__eq__' of Employee object at 0x0000020F61EF5520>),
# ('__format__', <built-in method __format__ of Employee object at 0x0000020F61EF5520>),
# ('__ge__', <method-wrapper '__ge__' of Employee object at 0x0000020F61EF5520>),
# ('__getattribute__', <method-wrapper '__getattribute__' of Employee object at 0x0000020F61EF5520>),
# ('__gt__', <method-wrapper '__gt__' of Employee object at 0x0000020F61EF5520>),
# ('__hash__', <method-wrapper '__hash__' of Employee object at 0x0000020F61EF5520>),
# ('__init__', <bound method Employee.__init__ of <__main__.Employee object at 0x0000020F61EF5520>>),
# ('__init_subclass__', <built-in method __init_subclass__ of type object at 0x0000020F61D86880>),
# ('__le__', <method-wrapper '__le__' of Employee object at 0x0000020F61EF5520>),
# ('__lt__', <method-wrapper '__lt__' of Employee object at 0x0000020F61EF5520>),
# ('__module__', '__main__'), ('__ne__', <method-wrapper '__ne__' of Employee object at 0x0000020F61EF5520>),
# ('__new__', <built-in method __new__ of type object at 0x00007FFBFAF3AB50>),
# ('__reduce__', <built-in method __reduce__ of Employee object at 0x0000020F61EF5520>),
# ('__reduce_ex__', <built-in method __reduce_ex__ of Employee object at 0x0000020F61EF5520>),
# ('__repr__', <method-wrapper '__repr__' of Employee object at 0x0000020F61EF5520>),
# ('__setattr__', <method-wrapper '__setattr__' of Employee object at 0x0000020F61EF5520>),
# ('__sizeof__', <built-in method __sizeof__ of Employee object at 0x0000020F61EF5520>),
# ('__str__', <method-wrapper '__str__' of Employee object at 0x0000020F61EF5520>),
# ('__subclasshook__', <built-in method __subclasshook__ of type object at 0x0000020F61D86880>),
# ('__weakref__', None), ('email', 'Arbaaz.khan@gmail.com'),
# ('explain', <bound method Employee.explain of <__main__.Employee object at 0x0000020F61EF5520>>),
# ('fname', 'Arbaaz'), ('lname', 'khan')]
