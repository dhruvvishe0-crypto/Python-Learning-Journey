# There are multiple arguments in a function
# 1) Positional Arguments 
# 2) Keyword Arguments
# 3) Default Arguments


# positional Arguments

def add(a,b,c):
    c = a+b+c
    print(c)

add(99,56,78)


# Default Argument

def multiply(a,b= 10):
    c= a*b
    print(c)

multiply(5,6)
multiply(7) 
# Another example of default argument

def greet(name="Harsh"):
    print(f"Hello {name}")

greet()
greet("Alice")

#Keyword Arguments

def student_info(name,age,grade):
    print(f" Hii {name}, You are Of {age} age and your grade is {grade} so congrats for that")
 
student_info (age = 21, grade = "A+" ,  name= "Harsh")
