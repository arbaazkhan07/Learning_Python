#list1 = ['C' , 'C++' , 'JAVA' , 'C#' , 'PYTHON']

        # Break statement

'''for x in list1 :
    print(x)
    if x == 'JAVA' :
        break

for x in list1 :
    if x == 'JAVA' :
        break
    print(x)'''



        # Continue Statement


'''for i in range(1,31) :
    if i % 3 == 0 :
        continue

    print(i)'''

        # Pass

'''for i in range(1,31) :
    if i%2!=0 :
        pass
    else :
        print(i)'''

        # break and continue

'''i = 0
while True :
    if i<5 :
        i = i + 1
        continue
    print(i)
    i=i+1
    if i>50 :
        break'''



while True :
    inn = int(input('Enter number : '))
    if inn >= 101:
        print('Above 100')
        break
    else :
        print('Try again')
        continue

