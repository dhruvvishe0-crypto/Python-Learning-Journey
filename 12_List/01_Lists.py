# # List is A ordered Mutable collection of items 
# # List is mutable, that means we can change the list after creation
# # List is a collection which is ordered and changeable. Allows duplicate members.


# # Creating a list 

# marks = [90,95,35,56,65]
# print(marks)

# # Accessing the List Elements 

# print(marks[3])  
# print(marks[2])
# print(marks[1])
# print(marks[0])
# print(marks[6]) # IndexError: list index out of range


# print(marks[2:4]) # Slicing the list

# # we create a list by using square bracket
# # ordered , mutable collection of items
# # duplicate values allow


# list_2 =[45,45,4,6,7,67]
# print(list_2)

# print(list_2[4])
# print(list_2[-3])
# print(list_2[0:3]) # slicing

# creating a list of 5 fruits and printing it 

fruits = ['Mango','apple','pineapple','watermelon','guava']

print(fruits) 
print(fruits[4])
print(fruits[-3])
print(fruits[:])
print(fruits[0:3])
print(fruits[1:2])
print(len(fruits))
fruits.append('orange')
print(fruits)
fruits.remove('apple')
print(fruits)

for fruits in fruits:
    print(fruits)