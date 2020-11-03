def decorator_function(name_function):
    def func():
        print("Before calling 'name' function")
        name_function()
        print("After calling 'name' function")

    return func


@decorator_function
def name():
    print('Arbaaz khan')


# or

# name = decorator_function(name)

name()
