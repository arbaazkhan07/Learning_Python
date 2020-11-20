from numpy import *

# One Dimentional Array & ndim
'''arr = array([1, 2, 3, 4])
print(arr)
print(arr.ndim)'''

# Two Dimentional Array & ndim
'''arr1 = array([(1, 2, 3, 4), (5, 6, 7, 8)])
print(arr1)
print(arr1.ndim)'''

'''# Three Dimentional Array & ndim
arr2 = array([(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)])     # This is also a Two Dimentional Array
print(arr2)
print(arr2.ndim)'''

# ItemSize

'''arr3 = array([(21, 34, 74), (21, 34, 74)])
print(arr3.itemsize)'''  # byte size of each elements

# DType

#print(arr3.dtype)  # Data Type of Array

# Size

#print(arr3.size)  # Size of an Array

# Shape

#print(arr3.shape)  # Shape of an Array

# ReShape

'''print(arr3)
a = arr3.reshape(3, 2)
print(a)'''

# Ways of creating Arrays in NumPy

# array()

'''a1 = array([1, 2, 3, 4])
print(a1)'''

# linspace()

'''a2 = linspace(0, 10, 5)  # Divide 5 parts in between 0 to 10
print(a2)'''

# arange()

'''a3 = arange(0, 10, 2)  # It will skip 1 number between 0 to 10
print(a3)
a4 = arange(5, 30, 5)  # It will skip 4 numbers between 0 to 30
print(a4)'''

# zeros() and ones()

'''a5 = zeros(10, int)  # Returns 10 ZEROS
print(a5)

a6 = ones(10, int)  # Return 10 ONES
print(a6)'''

# Concatinating

'''ac1 = array([1, 2, 3, 4, 5])
ac2 = array([6, 7, 8, 9, 10])

ac3 = concatenate([ac1, ac2])
print(ac3)
# or
print(concatenate([ac1, ac2]))'''
