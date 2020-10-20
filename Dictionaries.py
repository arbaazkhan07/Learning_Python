d = {
    'Name': 'Arbaaz khan',
    'Age': 23,
    'Year': 1998
}
print(d)

# Accessing items

dict0 = {
    'Name': 'Arbaaz khan',
    'Age': 23,
    'Year': 2000
}
print(dict0['Name'])

# get

print(dict0.get('Name'))

# Change values

c_v = dict0['Year'] = 1998
print(c_v)
print(dict0)

# Loop through a dict0ionary

# Keys
for x in dict0:
    print(x)

# Value
for x in dict0:
    print(dict0[x])

# Items
for x, y in dict0.items():
    print(x, y)

    # Check if item exists

if 'Name' in dict0:
    print("'Name' is exists")

    # Length

print(len(dict0))

# Adding items

dict0['Sex'] = 'Male'
print(dict0)

# Remove using POP

'''dict0.pop('Age')
print(dict0)

dict0.popitem()
print(dict0)'''

# Delete

'''del dict0['Sex']
print(dict0)

del dict0
print(dict0)'''

# Clear

'''dict0.clear()
print(dict0)'''

# Copy

dict1 = dict0.copy()
print(dict0)
print(dict1)

# Nested Dictionaries

n_dict = {
    'n1': {
        'Name': 'Arbaaz',
        'Age': 23
    },
    'n2': {
        'Name': 'Rohit',
        'Age': 22
    },
    'n3': {
        'Name': 'John',
        'Age': 20
    }
}

print(n_dict)

# OR

n1 = {
    'Name': 'Arbaaz',
    'Age': 23
}
n2 = {
    'Name': 'Rohit',
    'Age': 22
}
n3 = {
    'Name': 'John',
    'Age': 20
}

dicdic = {
    'Dictionary1': n1,
    'Dictionary2': n2,
    'Dictionary3': n3
}

print(dicdic)

# Fromkeys

var1 = ['Name', 'Age']
var2 = 0

dict2 = dict.fromkeys(var1, var2)
print(dict2)

# Keys

dict3 = {
    'Name': 'Arbaaz khan',
    'Age': 23,
    'Year': 1998
}

d3 = dict3.keys()
print(d3)

# update

dict3.update({'Sex': 'Male'})
print(dict3)

# Value

d4 = dict3.values()
print(d4)
