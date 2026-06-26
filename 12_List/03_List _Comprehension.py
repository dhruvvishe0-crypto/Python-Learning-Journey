#  # Create a list containing a square of numbers from 1 to 10

# squares = []

# for i in range(1,11):
#     squares.append(i**2)

# print(squares)

# # Now Lets See List Comprehension 

# squares_1 = [x **2 for x in range(1,11) ]

# print(squares_1)

# squares_2 = []

# for i in range(1,11):
#     squares_2.append(i**2)

# print(squares_2) 

# list comprehension is basically a way from which we can create a list in very short format 
# for example 

# squares_3 = [i ** 2 for i in range(1,11)]
# print(squares_3)

# numbers = [i*1 for i in range(1,11)]
# print(numbers)

# Squares = [i**2 for i in range(1,11)] 
# print(Squares)

# cubes = [i**3 for i in range(1,11)] 
# print(cubes)

# double = [i + i for i in range(1,11)] 
# print(double)


# first if use in list comprehension we need to create a list of even numbers only

# we are doing first normally then we will do list comprehension

# evens = []
# for i in range(1,21):
#     if i % 2 == 0 :
#         evens.append(i)

# print(evens)


# now we are doing list comprehension 

evens_1 = [i for i in range(1,21) if i % 2 == 0]
print(evens_1)



