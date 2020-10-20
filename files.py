"""
Modes of opening file in Python:
There are many modes of opening a file in Python, unlike other languages Python has provided its users a variety of
options. We will discuss seven of them in this tutorial.

r : r mode opens a file for read-only. We do not have permission to update or change any data in this mode.
w : w mode does not concern itself with what is present in the file. It just opens a file for writing and if there is
    already some data present in the file, it overwrites it.
x : x is used to create a new file. It does not work for an already existing file, as in such cases the operation fails.
a : a stands for append, which means to add something to the end of the file. It does exactly the same. It just adds
    the data we like in write(w) mode but instead of overwriting it just adds it to the end of the file. It also does
    not have the permission of reading the file.
t : t mode is used to open our file in text mode and only proper text files can be opened by it. It deals with the file
    data as a string.
b : b stands for binary and this mode can only open the binary files, that are read in bytes. The binary files include
    images, documents, or all other files that require specific software to be read.
+ : In plus mode, we can read and write a file simultaneously. The mode is mostly used in cases where we want to update
    our file.
"""

# Opening and Closing a file

'''f = open('File_opening')
print(f.read())
f.close()

f = open('File_opening')
print(f.read(5))

print(f.read(5))
f.close()'''

# or

'''with open('File_opening.txt') as f:
    print('1.', f.name, 'is the file name')  # File name
    print('2.', f.mode, 'is the file mode')  # file mode
    print('3.', f.read())

with open('File_opening.txt', 'r') as f1:
    # print(f1.readline())  # prints only one line
    # print(f1.readline())
    # print(f1.readline())
    # print(f1.readline())
    # print(f1.readline())
    # or
    for i in f1:
        print(i, end='')

print()
print()

with open('File_opening.txt', 'r') as f2:
    size_of_file = 50
    file_data = f2.read(size_of_file)
    while len(file_data) > 0:
        print(file_data, end=" || ")
        file_data = f2.read(size_of_file)
print()
with open('File_opening.txt', 'r') as f3:
    print(f3.readlines())'''

# By using modes

# r : r mode opens a file for read-only. We do not have permission to update or change any data in this mode.

'''f = open('File_opening.txt', 'r')
print(f.read())
f.close()'''

# t : t mode is used to open our file in text mode and only proper text files can be opened by it. It deals with the
#     file data as a string.

'''f = open('File_opening.txt', 'rt')  # Only 't' does't work
print(f.read())
f.close()'''

# w : w mode does not concern itself with what is present in the file. It just opens a file for writing and if there is
#     already some data present in the file, it overwrites it.

with open("File_Writing.txt", "w") as fw:
    fw.write("Hello! My name is khan..\n")
    fw.write("I'm 23 year old..\n")
    # size = fw.write("Hello! My name is khan..")
    # print(size)   #prints the size of text


# a : a stands for append, which means to add something to the end of the file. It does exactly the same. It just adds
#     the data we like in write(w) mode but instead of overwriting it just adds it to the end of the file. It also does
#     not have the permission of reading the file.

with open("File_Writing.txt", "a") as fw1:
    fw1.write("aaaaaaaaaaaaaaaaaaaaa\n")
    fw1.write("zzzzzzzzzzzzzzzzzzzzz\n")

# Both READ and WRITE

with open("File_Writing.txt", "r+") as rw:
    print(rw.read())
    rw.write('Bye bye')
    print(rw.read())