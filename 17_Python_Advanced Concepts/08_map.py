'''
Map is also called as high order function in python
It operators on the iterables(list,tuples,etc.)

Map function applies the given function to every item of an iterable and returns an iterator

'''

# For example

numbers = [45,55,8,6,2]  # this is am iterable (list)


def square(x):   # this is a given function
    return x*x


# we are applying given function to iterable each item
print(list(map(square,numbers)))  # we have to write list here to get output as list as map returns itself it doesnt return list

# another example

list_numbers = [4,6,3,7,3,8,0]
def cube(b):
    return b**3

print(list(map(cube,list_numbers)))






