# from numpy import *
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

from array import *

# 'i' and 'I'

var = array('I', [1, 2, 3, 4])
print(var)

var1 = array('i', [5, 6, -7, 8])
print(var1)

#