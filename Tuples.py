tuple = (1, 2, 3, 4, 5, 6)
print(tuple)

# Indexing

ind = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
print(ind[6])

# Negative Indexing

n_ind = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
print(n_ind[-6])

# Range of Index

r_ind = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
print(r_ind[2: 8])

# Range of Negative Indexing

r_n_ind = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
print(r_n_ind[-8: -2])

# Change tuple value

tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
lst = list(tpl)
print(lst)
lst[3] = 10
# tpl = tuple(lst)
print(lst)

# Loop through tuple

l_tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
for x in l_tpl:
    print(x)

    # Check if item exist

item = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
if 0 in item:
    print('0 is in the \'Tupel\'')

    # Length

length_tpl = (1, 2, 3, 4, 5)
print(len(length_tpl))

# Create tuple with one item

on_tpl = ('Arbaaz khan',)  # this is a tuple
print(on_tpl)
print(type(on_tpl))
on_tpl1 = ('Arbaaz khan')  # this is NOT a tuple
print(on_tpl1)
# pri(type(on_tpl1)) # ERROR

# Delete

delete_tpl = (1, 2, 3, 4, 5)
del delete_tpl
# print(delete_tpl) ### output will be name 'delete_tpl' is not defined

# Concatination

con_tpl = ('Arbaaz', 'khan')
con_tpl1 = (1, 2, 3, 4)
concate = con_tpl + con_tpl1
print(concate)

# Count

ct = (1, 2, 3, 4, 5, 5, 6, 7, 7)
print(ct.count(5))

# Index

inde_x = (1, 2, 3, 4)
print(inde_x.index(3))
