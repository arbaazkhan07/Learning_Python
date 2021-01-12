# Iterators

"""lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# for i in lst:
#     print(i)
it = iter(lst)
# print(it) ---> <list_iterator object at 0x0000013213C24A00>

print(next(it))
print(it.__next__())
print(next(it))
print(it.__next__())
print(next(it))
print(it.__next__())
print(next(it))
print(it.__next__())
print(next(it))
print(it.__next__())"""

###########

'''class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

for i in myclass:
    print(i)'''

# Generators

'''def TopTen():
    yield 1
    yield 2
    yield 3
    yield 4


val = TopTen()
# print(val.__next__())
# print(next(val))
print(val.__next__())
print(next(val))

for i in val:
    print(i)'''


######

def topten():
    n = 1
    while n <= 10:
        sq = n * n
        yield sq
        n += 1


val = topten()

for i in val:
    print(i)