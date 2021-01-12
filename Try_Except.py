print()
###
'''n1 = input('Enter 1st number: ')
n2 = input('Enter 2nd number: ')

try:
    print(int(n1) + int(n2))

except Exception as a:
    print(a)

print('Try_Except runnig..')'''
###

'''try:
    f = open('asdf.py')
except Exception:
    print("File does not exist.")'''

# Try_Except with Else

'''try:
    f = open('Examples.py')
except Exception:
    print("File does not exist.")
else:
    print(f.read())
    f.close()'''

# Try_Except with Else and Finally

'''try:
    f = open('asdfs.py')
except Exception:
    print("File does not exist.")
else:
    print(f.read())
    f.close()
finally:
    print("Don't worry move on..")'''

#####

'''a = 5
b = 0

try:
    print(a/b)

except Exception:
    print('You can not Divide nuber by Zero')

print('Bye')'''

#####

'''a = 5
b = 0

try:
    print('Resource Open..')
    print(a/b)

except Exception as e:
    print('You can not Divide number by Zero :', e)

finally:
    print('Resource close..')
    
print('Bye')'''

#####

num1 = input('Enter 1st number:')
num2 = input('Enter 2nd number:')

try:
    print('Resource Open..')
    print(int(num1) / int(num2))

except ZeroDivisionError as e:
    print('You can not Divide number by Zero :', e)

except ValueError as e:
    print('Invalid Input..')

except Exception:
    print('Something went wrong..')

finally:
    print('Resource close..')

print('Bye')
