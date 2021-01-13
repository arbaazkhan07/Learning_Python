###########

"""class Hello():
    def run(self):
        for i in range(5):
            print('Hello')


class Hi():
    def run(self):
        for i in range(5):
            print('Hi')


h1 = Hello()
h2 = Hi()

h1.run()
h2.run()"""

###############

'''from threading import *


class Hello(Thread):
    def run(self):
        for i in range(500):
            print('Hello')


class Hi(Thread):
    def run(self):
        for i in range(500):
            print('Hi')


h1 = Hello()
h2 = Hi()

h1.start()
h2.start()'''


###################

'''from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
            print('Hello')
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print('Hi')
            sleep(1)


h1 = Hello()
h2 = Hi()

h1.start()
sleep(0.3)
h2.start()

print('Bye')'''

#######################

from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
            print('Hello')
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print('Hi')
            sleep(1)


h1 = Hello()
h2 = Hi()

h1.start()
sleep(0.3)
h2.start()

h1.join()
h2.join()

print('Bye')
