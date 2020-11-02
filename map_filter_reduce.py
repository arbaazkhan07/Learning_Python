######################### map() #########################

"""num = ['23', '54', '78', '12', '6', '33']  # List of Strings
print(num)
num = map(int, num)  # Converting Strings into Integers
print(num)
num = list(map(int, num))  # Putting Integers in a List
print(num)"""

####

'''def sq(n):
    return n * n


lst = [2, 3, 4, 5, 6, 7, 8, 9]
lst = list(map(sq, lst))
print(lst)'''

####

'''lst = [2, 3, 4, 5, 6, 7, 8, 9]
lst = list(map(lambda n: n * n, lst))
print(lst)'''

####

'''def squre(s):
    return s * s


def cube(c):
    return c * c * c


lst = [squre, cube]
lst1 = [2, 3, 4, 5, 6, 7, 8, 9]
for i in lst1:
    var = list(map(lambda l: l(i), lst))
    print(var)'''

######################### filter() #########################

'''def greater(g):
    return g > 5


lst = [2, 3, 4, 5, 6, 7, 8, 9]
lst = list(filter(greater, lst))
print(lst)'''

######################### reduce() #########################

'''from functools import reduce  # Importing REDUCE

lst = [2, 3, 4, 5, 6, 7, 8, 9]
lst = reduce(lambda a, b: a + b, lst)
print(lst)'''
