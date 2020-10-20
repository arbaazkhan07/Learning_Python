a = 'Arbaaz'
b = "khan"

print(a)
print(b)

# multistring

multi = '''Myself Arbaaz khan & I am 23 years old,
I'm a SOFTWARE ENGINEER and
I love PROGRAMING...'''
print(multi)

# String Array

array = 'Arbaaz khan'
print(array[0] + array[7])

# String Slicing

slice = 'Arbaaz khan'
print(slice[7: 11])

# String Length

length = 'Arbaaz khan'
print(len(length))

# Strip

Strip = '     Arbaaz khan     '
print(Strip)
print(Strip.strip())

# Lower

low = 'Arbaaz Khan'
print(low.lower())

# Upper

upp = 'Arbaaz khan'
print(upp.upper())

# Replace

rep = 'Arbaaz khan'
print(rep.replace('b', 'g'))

# Split

Split = 'Arbaaz, khan'  # , must be inserted
print(Split.split(','))

# String check

s_check = 'Arbaaz khan'
print('aaz' in s_check)

x = 'Armaan' in s_check
print(x)

print('aaz' not in s_check)
print('Armaan' not in s_check)

# String Concatination

# String to String
s_concat0 = 'Arbaaz'
s_concat1 = 'khan'
print(s_concat0 + s_concat1)

# String to Number
age = 23
age1 = 50
name = 'My age is {}'
print(name.format(age))
print('My age is {}'.format(age))
print('My age is {} and Her age is {}'.format(age, age1))
print('My age is {1} and Her age is {0}'.format(age1, age))

# Escape Charactor

print('My name is \'Arbaaz khan\' or My name is \"Arbaaz khan\"')  # \'\' or \"\"
print('It\'s me \'AK\' or It\'s me \"AK\"')  # \' and \'\' or \' and \"\"



