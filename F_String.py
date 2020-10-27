name = 'Arbaaz khan'
print('1. My name is %s' % name)

#

name1 = 'Arbaaz khan'
st = 'and age is'
age = 23
print('2. My name is %s %s %s' % (name1, st, age))

#

name2 = 'Arbaaz khan'
st1 = 'and age is'
age1 = 24
print('3. My name is {} {} {}'.format(name2, st1, age1))
print('4. My name is {2} {1} {0}'.format(name2, st1, age1))

# F String

name3 = 'Arbaaz khan'
st2 = 'and age is'
age2 = 24
print(f'5. My name is {name3} {st2} {age2}')

#

name4 = 'Arbaaz khan'
st3 = 'and age is'
age3 = 24
print(f'6. My name is {name4} {st3} {age3} {5 + 5}')

# or

ad = lambda x, y: x + y
name5 = 'Arbaaz khan'
st4 = 'and age is'
age4 = 24
print(f'7. My name is {name5} {st4} {age4} {ad(3, 4)}')
