# Typecasting is the process of converting one data type to another 
# In Python, you can use the built-in functions int(), float(), str(), and bool() to perform typecasting.


# integer = whole numbers 
# float = Always in decimal form
# string = always in quotes 
# boolean = True or False


#syntax of typecasting is:
#  a = 34  we need to convert a to string 
#  b = str(a)
# This will convert a a to the string type 
#  print(b)     output will be "34"

# Typecasting Example

# 1. Converting  Integer to String 
int_number = 1111
str_number = str(int_number)    # Convert integer to string
print(str_number)
print(type(str_number)) # This will print the data type of the variable 

#2 Converting String To Integer 
Str_number = "2222"
Int_number = int(Str_number)     # Convert string to integer
print(Int_number)
print(type(Int_number))

#3 Integer to Float 
int1_num = 3333
float_num = float(int1_num)    # Convert integer to float`
print(float_num)
print(type(float_num))

#4 Float to Integer
Float_num = 5555.55
Int2_num = int(Float_num)
print(Int2_num)
print(type(Int2_num))

#5 String to Float
str_num = "65"
float_num2 = float(str_num)   # Convert string to float
print(float_num2)
print(type(float_num2))

#6 Float to String
float_num3 = 77.77
str_num3 = str((float_num3))  # Convert float to string
print(str_num3)
print(type(str_num3))

