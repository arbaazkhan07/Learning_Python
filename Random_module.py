from random import *

# randint()

rand = randint(1, 6)
print(rand)

# random()

rand1 = random()  # 0 and 1
print(rand1)

rand2 = random() * 100  # 0 to 100
print(rand2)

# choice()

lst = ['Arbaaz khan', 'Rohit', 'Vikas', 'Nisarg', 'Maaz']
rand3 = choice(lst)
print(rand3)
