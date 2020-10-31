"""list0 = [['C' , 'is better'] ,
        ['C++' , 'is better than C'] ,
        ['JAVA' , 'is better than C++'] ,
        ['C#' , 'is better than JAVA'] ,
        ['PYTHON' , 'is better than C#']]
dict0 = dict(list0)
print(dict0)
for x , y in list0 :
    print(x , y)

for x, y in dict0.items():
    print(x, y)

for x in dict0.keys():
    print(x)

for x in dict0.values():
    print(x)"""

'''lst = ['Arbaaz' , 'Khan' , 1 , 2 ,3 , 4 , 5 , 6 , 5 , 9 , 8 , 0 , 7 , 8 , 34 , 44 , 65 , 87 , 2345]
for item in lst :
    if str(item).isnumeric() and item > 6 :
        print(item)'''

'''list = ['Eggs', 'chicken', 5050, 12,56,345,35355]
for list in list:
    if(type(list) == int and list>6) :
        print(list)

    if (type(list) == str) :
        print(list)'''

# RANGE
'''for i in range(10) :
    print(i)

for i in range(21 , 31) :
    print(i)

for i in range( 31, 41 , 2) :
    print(i)'''

# TABLE

'''num = int(input('Enter a number : '))
for i in range(1 , 11) :
    table = num * i
    print(num , '*' , i , '=' , table)

        # REVERSE TABLE
for i in range(1 , 11 , -1) :
    table = num * i
    print(num , '*' , i , '=' , table)'''

# Sum of numbers
'''sum = 0
for i in range(1 , 101) :
    sum = sum + i
print(sum)'''

# END=''

# list1 = ['C' , 'C++' , 'JAVA' , 'C#' , 'PYTHON']
'''for x in list1 :
    print(x, end=' ')

print()
# Loop through a string

for x in 'PYTHON' :
    print(x)'''

# for with else

'''student = 'Nisarg'
marks = {
    'Arbaaz': {'C': 98, 'JAVA': 99, 'PYTHON': 100},
    'Maaz': {'C': 50, 'JAVA': 60, 'PYTHON': 70},
    'Rohit': {'C': 40, 'JAVA': 50, 'PYTHON': 60}
}
for i in marks.items():
    print(i)
    if i == student:
        print(i)
else:
    print('Nisarg is DEAD')'''

##########

lis = ['Arbaaz khan', 'Shah Rukh Khan', 'Salman khan', 'Amir khan']

for i in lis:
    print(i, 'and', end=' ')

# Join function

print()
j = ' and '.join(lis)
print(j)
