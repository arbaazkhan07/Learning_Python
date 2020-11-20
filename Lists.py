lst = ['Apple', 'Banana', 'Cherry']
print(lst)

# Indexing

a_list = ['Apple', 'Banana', 'Cherry']
print(a_list[2])

# Nagative Indexing

n_ind = ['Apple', 'Banana', 'Cherry']
print(n_ind[-3])

# Range of Indexing

r_ind = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(r_ind[1:5])
print(r_ind[:4])
print(r_ind[2:])

# Range of Negative Indexing

n_ind1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(n_ind1[-6:-4])

# Change Item Value

i_value = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
i_value[2] = 'Strowberry'
print(i_value)

# Loop through a List

l_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
for x in l_list:
    print(x)

    # Check if item exist

e_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
if "cherry" in e_list:
    print("Yes, Cherry is in the list.. ")

    # Length

length = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(len(length))

# Append

a_end = ["apple", "banana", "cherry", "orange"]
a_end.append('Mango')
print(a_end)

# Insert

ins = ["apple", "banana", "cherry", "orange"]
ins.insert(2, 'Kiwi')
print(ins)

# Remove

rem = ["apple", "banana", "cherry", "orange"]
rem.remove('banana')
print(rem)

# POP

p = ["apple", "banana", "cherry", "orange"]
p.pop()
# p.pop(1)
print(p)

# DELLETE

delete = ["apple", "banana", "cherry", "orange"]
del delete[1]
print(delete)

delete1 = ["apple", "banana", "cherry", "orange"]
del delete1
# print(delete1) # Error will be : delete1 is not defined

# Clear

clr = ["apple", "banana", "cherry", "orange"]
clr.clear()
print(clr)

# Copy List

cp = ["apple", "banana", "cherry", "orange"]
cp1 = cp.copy()
print(cp)
print(cp1)

'''li = ["apple", "banana", "cherry", "orange"]
li1 = list(li)
print(li)
print(li1)'''

# Concatinations

# + operator
lst1 = ["apple", "banana", "cherry", "orange"]
lst2 = [1, 2, 3]
lst3 = lst1 + lst2
print(lst3)

# For
'''for x in lst2 :
    lst1.append(x)

print(lst1)'''

# Extend
lst1.extend(lst2)
print(lst1)

# Count

lstc = [1, 2, 3, 4, 4]
c = lstc.count(4)
print(c)
