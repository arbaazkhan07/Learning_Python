# Addition
"""num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))

num3 = num1 + num2

print('Sum of your numbers:',num3)


            #

print("Enter first number")
num1 = input()
print("Enter second number")
num2 = input()
print(num1, end='+')
print(num2, end='=')
print(int(num1) + int(num2))"""

# Slicing

'''Name = 'Arbaaz khan'

Name = 'Arbaaz khan'

print('1.',len(Name))
print('2.',Name[3 : 8])
print('3.',Name[ : 8])
print('4.',Name[0 : ])
print('5.',Name[0 : 11 : ])
print('6.',Name[0 : 11 : 2])
print('7.',Name[ :  : ])
print('8.',Name[4 :  : ])


demo="Akash is a good boy"
print(demo.count(""))
#output=20'''

'''d1={"vishnu":"god","house":"home","mom":["mother","maa","mummy"]}
print(d1)
#take input from user
print("input any of three vishnu/house/mom")
print(d1[input()])'''

# Dictionary
''''dictionary = {
    'List': 'List is a collection which is ordered and changeable. Allows duplicate members.',
    'Tuple': 'Tuple is a collection which is ordered and unchangeable. Allows duplicate members.',
    'Set': 'Set is a collection which is unordered and unindexed. No duplicate members.',
    'Dictionary': 'Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.'
}
'''
# print(dictionary.keys())

'''print('Enter the options geven below\n\n1.List\n2.Tuple\n3.Set\n4.Dictionary')

# User input
userin = input()

# Checking KEYS and printing VALUES
if userin in dictionary.keys():
    print(dictionary[userin])
else:
    print('Oops! Invalid option')'''

'''mean={
    "set":"A set is a group of things that belong together",
    "accumulation":"the acquisition or gradual gathering of something",
    "access":"an attack or outburst of an emotion",
    "power":"the ability or capacity to do something or act in a particular way"}
print("Enter your word: ")
var=input()
if var in mean:
    print(mean[var])
else:
    print("Wrong input")'''

# Foulty Calculator

'''num1 = int(input('Enter 1st number..\n'))
num2 = int(input('Enter 2nd number..\n'))
oper = input('Enter operator given below : \n+\n*\n/\n')

#45 * 3 = 555
#56+9 = 77
#56/6 = 4

if  num1 == 45 and num2 == 3 and oper == '*':
    print('45 * 3 = 555')
elif num1 == 56 and num2 == 9 and oper == '+':
    print('56+9 = 77')
elif num1 == 56 and num2 == 6 and oper == '/':
    print('56/6 = 4')
else :
    if oper == '+':
        num3 = num1 + num2
        print(num1, '+', num2, '=', num3)
    elif oper == '*':
        num3 = num1 * num2
        print(num1, '*', num2, '=', num3)
    elif oper == '/':
        num3 = num1 / num2
        print(num1, '/', num2, '=', num3)
    else:
        print('Please enter the given operators..')'''

# Guessing Numbers (GAME)

real = 6
guess = 0

print('\t\t\t\tGuess the REAL number\n')

for guess in range(5):
    in_num = int(input('Enter your number below...\n'))
    # print('Number of guess remain', 5 - guess)
    if real > in_num:
        print('Smaller guess')
        print('Guess left :', 4 - guess)
        continue
    elif in_num > real:
        print('Greater guess')
        print('Guess left :', 4 - guess)
        continue
    else:
        print('Right guess.. GAME OVER')
        print('You saved', 4 - guess, 'guesses..')
        break

# Prime or not

'''n = 0
while n == 0:
    num = int(input('Enter nuber to check PRIME or not :\n'))
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(num, 'is a NON-PRIME number')
                break
        else:
            print(num, 'is a PRIME number')
    else:
        print('0 , 1 or Nagetive numbers are already NON-PRIME numbers..\nPls enter positive numbers above 1..')
        continue
    break'''