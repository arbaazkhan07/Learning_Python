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
