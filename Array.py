from array import *

"""
Type code	C Type	 	        Python Type		            Minimum size in bytes

'b'		    signed char		      int		   	                    1

'B'		    unsigned char		  int	   		                    1

'u'		    wchar_t			      Unicode character   	            2

'h'		    signed short		  int		   	                    2

'H'		    unsigned short		  int	   		                    2

'i'		    signed int		      int		   	                    2

'I'		    unsigned int		  int		   	                    2

'l'		    signed long 		  int		   	                    4

'L'		    unsigned long		  int	   		                    4

'q'		    signed long long	  int	   		                    8

'Q'		    unsigned long long	  int	  		                    8

'f'		    float	 		      float		  	                    4

'd'		    double			      float		  	                    8
"""

# 'i' and 'I'

var = array('I', [1, 2, 3, 4])
print(var)

var1 = array('i', [5, 6, -7, 8])
print(var1)

# Buffer info

print(var.buffer_info())

# Typecode

print(var.typecode)
print(var1.typecode)

# Append

var.append(9)
print(var)
var1.append(10)
print(var1)

# Reverse

var.reverse()
var1.reverse()
print(var)
print(var1)

# Indexing

print(var[0])

for i in range(5):
    print(var[i], end=" ")

print()

for i in range(5):
    print(var1[i], end=" ")

print()

# or

for i in range(len(var)):
    print(var[i], end=" ")

print()

for i in range(len(var1)):
    print(var1[i], end=" ")

print()

# or

for i in var:
    print(i, end=" ")

print()

for i in var1:
    print(i, end=" ")

print()

# 'u'

var2 = array('u', ['A', 'e', 'i', 'o', 'u'])
print(var2)
