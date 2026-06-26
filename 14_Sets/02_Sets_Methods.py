set_1 = {6, 7, 4, 3, 8}

print(set_1)
print(type(set_1))
set_1.add(98)
set_1.discard(7)  # safer than remove
set_1.pop()       # removes a random element
print(set_1)

# doing revision 
# a set have mainly 3 methods and these are 
# 1) discard = it is better than remove 
# 2) add - which adds the elements
# 3) pop = which deletes the random element

set_2 = {56,78,45,67}
print(set_2)
set_2.add(98)
set_2.discard(56)
print(set_2)
set_2.pop()
print(set_2)

