'''

Exceptions are events that occur during the execution of a program that disrupt
the normal flow of instructions. Python provides a robust mechanism for handling
exceptions using try-except blocks. This allows your program to gracefully
recover from errors or unexpected situations, preventing crashes and providing
informative error messages. You can also define your own custom exceptions to
represent specific error conditions in your application.

'''

# we use try and except blocks to handle this exceptions

# in try block it contains the code that has to be used also it can raise an exception
# to handle the exception we use except block lets see by writing codes


# we will take two numbers as input and will do some of them repeadetly using while loop

# while True:
#     number_1 = int(input("Enter Number one : "))
#     number_2 = int(input("Enter Number Two : "))

#     print(f"The sum of two numbers is {number_1 + number_2}")

# now it works properly but what if anyone tries to add a string lets see what happens

''' File "d:\Python Learning Journey\17_Python_Advanced Concepts\06_Try_Except_errors.py", line 22, in <module>
    number_2 = int(input("Enter Number Two : "))
ValueError: invalid literal for int() with base 10: 'dhruv'''

# this error comes and whole code crashes so to avoid the crash we use try and except

# while True:

#     try:                   # if no error occured then it will run smoothly
#         number_3 = int(input("Enter Number one : "))
#         number_4 = int(input("Enter Number Two : "))
#         print(f"The sum of two numbers is {number_3 + number_4}")

#     except:  # if any error happens in try then this except block gives this message and also code doesn't crashes
#         print("some error occured")

# also you can specify a exception like these


# while True:

#     try:                   # if no error occured then it will run smoothly
#         number_5 = int(input("Enter Number one : "))
#         number_6 = int(input("Enter Number Two : "))
#         print(f"The division of two numbers is {number_5 / number_6}")


#     except ValueError:
#         print("Please Enter a Valid Number")

#     except ZeroDivisionError:
#         print("You cannot divide a number by zero")

#     except Exception as e:  # if any error happens in try then this except block gives this message of why code crashed 
#         print("Some error occured..... The error : ", e)

#     except:  # if any error happens in try then this except block gives this message and also code doesn't crashes
#         print("some error occured")


# you can also raise a custom error

num1= int(input("enter a number : "))
num2= int(input("enter another number : "))

if num2 == 0 :
    raise ZeroDivisionError("You cannot divide a number by zero")
print("the division of two numbers is : ",num1/num2)





