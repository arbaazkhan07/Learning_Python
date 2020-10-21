from numpy import *

# One Dimentional Array & ndim
arr = array([1, 2, 3, 4])
print(arr)
print(arr.ndim)

# Two Dimentional Array & ndim
arr1 = array([(1, 2, 3, 4), (5, 6, 7, 8)])
print(arr1)
print(arr1.ndim)

'''# Three Dimentional Array & ndim
arr2 = array([(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)])     # This is also a Two Dimentional Array
print(arr2)
print(arr2.ndim)'''

# ItemSize

arr3 = array([(21, 34, 74), (21, 34, 74)])
print(arr3.itemsize)  # byte size of each elements

# DType

print(arr3.dtype)  # Data Type of Array

# Size

print(arr3.size)  # Size of an Array

# Shape

print(arr3.shape)  # Shape of an Array

# ReShape

print(arr3)
a = arr3.reshape(3, 2)
print(a)
