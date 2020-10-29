from time import *

'''tm = time()
print(tm)
for i in range(500):
    print('Hello')
    # print(time())

print(time() - tm)'''


# Real time


real = asctime(localtime(time()))
print(real)

# sleep()

for i in range(5):
    print('Hello')
    sleep(1)