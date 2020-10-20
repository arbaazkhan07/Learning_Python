set_ = {'Arbaaz', 'khan', 'Engineer'}
print(set_)

# Loop through a SET

l_s = {'Arbaaz', 'khan', 'Engineer'}
for x in l_s:
    print(x)

    # Check if item in SET

i_c = {'Arbaaz', 'khan', 'Engineer'}
print('Arbaaz' in i_c)

if 'AK' not in i_c:
    print('AK is no more...')

    # ADD

addset = {1, 2, 3, 4}
addset.add(5)
print(addset)

# UPDATE

up_set = {1, 2, 3, 4}
up_set1 = {'Arbaaz', 'khan', 'Engineer'}
up_set.update([5, 6, 7, 8])
up_set1.update(['Python', 'Programing'])
print(up_set)
print(up_set1)

# Remove

rem = {1, 2, 3, 4}
rem.remove(3)
print(rem)

# Discard

dsk = {1, 2, 3, 4}
dsk.discard(2)
print(dsk)

# POP

pp = {1, 2, 3, 4}
pp.pop()
print(pp)

# clear

clr = {1, 2, 3, 4}
clr.clear()
print(clr)

# DELETE

dell = {1, 2, 3, 4}
del dell
# print(dell) ### Error : name 'dell' is not defined

# Concatination

'''addi = {1 , 2 , 3 , 4}
addi1 = {'Arbaaz' , 'khan' , 'Engineer'}
res = addi + addi1
print(res)'''  # TypeError: unsupported operand type(s) for +: 'set' and 'set'

# union

addi = {1, 2, 3, 4}
addi1 = {'Arbaaz', 'khan', 'Engineer'}
print(addi.union(addi1))

# update

addi2 = {1, 2, 3, 4}
addi3 = {'Arbaaz', 'khan', 'Engineer'}
addi2.update(addi3)
print(addi2)
