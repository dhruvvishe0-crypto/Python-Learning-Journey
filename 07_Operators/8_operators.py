# Types of Operators in Python
# 1. Arithmetic Operators
# 2. Comparison Operators
# 3. Logical Operators
# 4. Assignment Operators
# 5. Membership Operators
# 6. Identity Operators

#  Arithmetic Operator :
#  Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, and division.
#  The arithmetic operators in Python are:
#  + : Addition
#  - : Subtraction
#  * : Multiplication
#  / : Division
#  % : Modulo (Remainder)
#  // : Floor Division
# ** : Exponentiation (Power)

# Example:
a = 10

b = 9

print("a +b = ",a+b) # Addition
print("a -b = ",a-b) # Subtraction
print("a*b = ",a*b) # Multiplication
print("a /b = ",a/b) #  Division
print("a % b = ",a%b) # Modulo (Remainder)
print("a // b = ",a // b) # Floor Division
print("a ** b = ",a**b) #   Exponentiation (Power)

# Comparison operators :
# Comparison operators are used compare values and give true or false (boolean)
# The comparison operators in Python are:
# == : Equal To
# =! ; Not Equal to
# < : less than
# > : greater than
# <= : less than or equal to
# >= : greater than or equal to
# For example:

print(a==b) # Equal To
print(a!=b) # Not Equal to
print(a<b) # less than
print(a>b) # greater than
print(a<=b) # less than or equal to
print(a>=b) # greater than or equal to

# Logical Operators :
# Logical operators are used to combine conditional statements.
# The logical operators in Python are:
# and : Returns True if both statements are true and If any one of it is false then it returns false
# or : Returns True if one of the statements is true and If both are false then it returns false nets
# not : Returns True if the statement is false and returns false if the statement is true
# For example:
print("    ")
print(" And Operator :")
a = 25
print(a > 0 and a < 30) # if any of it is false then it returns false
print("    ")

print(" Or Operator :")

print ()

print(a >0 or a == 30) # if any of it is true then it returns true

print(a < 0 or a == 30) # if both are false it returns false

# assignment operators :
# Assignment operators are used to assign values to variables.
# The assignment operators in Python are:
# = : Assigns the value on the right to the variable on the left
# += : Adds the value on the right to the variable on the left and assigns the result to the variable on the left
# -= : Subtracts the value on the right from the variable on the left and assigns
# *= : Multiplies the variable on the left by the value on the right and assigns the result to the variable on the left
# /= : Divides the variable on the left by the value on the right and assigns the result to the variable on the left
# %= : Takes the modulo of the variable on the left by the value on the right and
#\\= : Takes the floor division of the variable on the left by the value on the right and assigns the result to the variable on the left

# Examples :

x = 67
print (x)
x+=5 # Adds 5 to x and assigns the result to x
print(x)

x -= 10 # Subtracts 10 from x and assigns the result to x
print(x)

x *= 10 # Multiplies x by 10 and assigns the result to x
print(x)

x %= 20 # Takes the modulo of x by 20 and assigns the result to x
print(x)

x /= 5 # Divides x by 5 and assigns the result to x
print(x)

x //= 4 # Takes the floor division of x by 4 and assigns the result to x
print(x)