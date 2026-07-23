'''
The reduce() function applies a function of two arguments cumulatively to the
items of an iterable from left to right

so as to reduce the iterable to a single value

reduce is not a built-in function it must be imported from the functools
module
'''

from functools import reduce

numbers = [3,4,5,6,7,8]
#         [7,5,6,7,8]    # this is how reduce works
#         [12,6,7,8]
#         [18,7,8]
#         [25,8]
#         [33]

def sum(a,b):
    return a+b

print(reduce(sum,numbers))