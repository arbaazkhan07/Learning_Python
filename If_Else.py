# IF

a = 33
b = 200
c = 500
if b > a:
    print("b is greater than a")

    # ELSE

if a > b:
    print('A is greater than B')
else:
    print('B is greater than A')

    # ELIF

if a > b:
    print('A is greater than B')
elif a == b:
    print('A is equals to B')
else:
    print('A is smaller than B')

    # Short hand IF

if a < b: print('{} is smaller than {}'.format(a, b))

# Short hand IF..ELSE

print('{} is greater than {}'.format(a, b)) if a > b else print('{} is smaller than {}'.format(a, b))

# Multiple statements

print('{} is greater than {}'.format(a, b)) if a > b else print(
    '{} is smaller than {}'.format(a, b)) if a < b else print('Both are Equal..')

# AND

if a < b and b < c:
    print('{} is smaller than {} AND {} is smaller than {}'.format(a, b, b, c))
else:
    print('{} , {} and {} are Equal'.format(a, b, c))

    # OR

if a < b or c > b:
    print('{} is smaller than {} OR {} is greater than {}'.format(a, b, c, b))
else:
    print('{} , {} and {} are Equal'.format(a, b, c))

    # Nested if

if a < b and b < c:
    print('{} is smaller than {} AND {} is smaller than {}'.format(a, b, b, c))
    if a < b or c > b:
        print('{} is smaller than {} OR {} is greater than {}'.format(a, b, c, b))
    else:
        print('{} , {} and {} are Equal'.format(a, b, c))

    # PASS

a1 = 33
b1 = 200

if b1 > a1:
    pass  # output will be nothing

    # Example

age = int(input('Enter your AGE :'))

if age > 18 and age < 101:
    print('You are 18 above and you can drive...')
elif age < 18 and age > 7:
    print("You are under 18 and you can't drive...")
elif age == 18:
    print("You are 18 and w'll think about it...")
else :
    print('Yor are a child...')

'''elif age > -1 and age < 1 :
    print("0 is not a age BITCH...")'''
