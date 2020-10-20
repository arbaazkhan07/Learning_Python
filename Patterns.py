# print('# # # #\n# # # #\n# # # #\n# # # #\n')

# # # #
# # # #
# # # #
# # # #

"""for i in range(4) :
    for j in range(4) :
        print('# ',end='')
    print()

pat1 =0
while pat1<4:
    pat = 0
    while pat<4:
        print('# ',end='')
        pat+=1
    print()
    pat1+=1"""

# print('#\n# #\n# # #\n# # # #\n')

#
# #
# # #
# # # #

'''for i in range(4):
    for j in range(i+1):
        print('# ',end='')
    print()'''

# print('# # # #\n# # #\n# #\n#\n')

# # # #
# # #
# #
#

'''for i in range(4):
    for j in range(4-i):
        print('# ',end='')
    print()'''

#  Pattern Exercize

num1 = int(input('Enter number:'))
num2 = int(input('Enter 1 or 2 for TRUE or FALSE:'))
# t_f = bool(num2)

if num2 == 1:
    for i in range(num1):
        for j in range(i + 1):
            print("*", end="")
        print()
elif num2 == 2:
    for i in range(num1):
        for j in range(4 - i):
            print("*", end="")
        print()
else:
    print("Plz enter 1 or 2 only..")
