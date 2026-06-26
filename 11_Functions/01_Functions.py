# # Functions are created by using the def keyword 
# # Syntax Of Creating A Function :
# # def function_name(parameters):
# #     code block
# #     return value (Optional)


# # I Want to create a normal greeting function 
# name = str(input("Enter Your Name:"))

# def greet(name):
#     print(f"Hello,{name},! Welcome To Our Website")

# greet(name)



#  # Now I am Creating A Function That Takes two Numbers And Returns Their Sum

# def add_numbers(num1,num2):
#     result = num1+num2
#     print(result)

# add_numbers(99,50)
# add_numbers(999,999)

# def add_numbers(num1,num2):
#     result = num1+num2
#     return result

# print(add_numbers(99,99))
# add_numbers(99,100)

# # Now i am Creating a function where a we take input from user of name and age and we gives output of Hey name you are too young that your age is just age 

# name = str(input("Enter Your Name :"))
# age = int(input("Enter Your Age :"))

# def user_input(name,age):
#     print(f"Hey {name} You are too young that your age is just {age} ")
# user_input(name,age)

# # Creating a function that takes multiple numbers and returns their multiplication

# def multiply_numbers(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10):
#     result =  num1*num2*num3*num4*num5*num6*num7*num8*num9*num10
#     print(result)

# multiply_numbers(1,2,3,4,5,6,7,8,9,10)



# #Creating a function that gives square of any number

# def square_number(number):
#     result = number**2
#     print(result)

# square_number(73)
# square_number(79)

# # Creating a Function That takes input and tells whether the number is even or odd


# number = int(input("Enter a Number to check whether it is odd or even :"))

# def check_even_odd(number):
#      if number %2==0:
#           print(f"{number} is an Even Number ")
#      else :
#           print (f"{number} is an odd number ")

# check_even_odd(number)





# def numbers(num3,num4):
#     result = num3 * num4
#     print(result)

# numbers(4,20)




# name = str(input("Enter Your Name :"))
# age =  int(input("Enter Your Age : "))

# def nationality_Certificate(name,age):
#     print(f"Your Name IS {name} And Your Age is {age} So We see The Data Of Our Countries Citizens List It Proves That You Are From India")

# nationality_Certificate(name,age)

# Number2 = int(input("Enter A Number To Check Whether It is Odd Or Even : "))

# def even_odd_Number_Check(Number2):
#     if Number2 % 2 ==0 :
#         print(f"{Number2} It is The Even Number")
#     else :
#         print(f"{Number2} It is The Odd Number")

# even_odd_Number_Check(Number2)

# num = int(input("Enter A Number To Find It's Square :"))

# def Square_of_Number(num):
#     print(f"The Square of the {num} is", num *num)

# Square_of_Number(num)


# name = str(input("enter your name : ".title()))

# def greet(name):
#     print(f"hello {name} , welcome to our website hope you will like it".title())

# greet(name)



# Taking Marks as a Input and giving grades according to the marks 

# marks = int(input("enter your marks : ".title()))

# def grades(marks):
    
#     if marks >= 90 :
#         print("congratulations you got grade a ".title())

#     elif marks >= 75 : 
#         print("congratulations you got grade b ".title())

#     elif marks >= 50 : 
#         print("congratulations you got grade c".title())

#     else: 
#         print("Sorry You are failed".title())

# grades(marks)


# a function that give any table

# number = int(input("Enter your number : ".title()))

# def table(number):
#     for i in range(1,11):
#         print(f"{number} X ", i ,  " = ", number * i )

    
# table(number)

# creating the function that doubles the number 
# number = int(input("enter a number to make it double : ".title()))

# def double(number):
#     double_2 = number + number 
#     print(f"the double of {number} is = ".title(),double_2)

# double(number)
# A function that gives the cube of number 
# number_1 = int(input("enter a number to get cube of it : ".title()))

# def cube(number_1):
#     cube_1 = number_1 ** 3
#     print(f"The Cube of {number_1} is = ".title(),cube_1)

# cube(number_1)

# Now practising return 

# number_1 = int(input("enter a number to get sum of it : ".title()))
# number_2 = int(input("enter a number to get sum of it : ".title()))

# def sums(number_1,number_2):
#     result = number_1 + number_2
#     return result

# answers = sums(number_1,number_2)
# print(answers)


# number_1 = int(input("enter a number to get largest  : ".title()))
# number_2 = int(input("enter a number to get largest : ".title()))

# def largests(number_1,number_2):
#     if number_1> number_2 :
#         print(f"{number_1} is a greater than {number_2}")

#     else:
#         print(f"{number_2} is a greater than {number_1}")
 
 
# answers = largests(number_1,number_2)
# print(answers)

# #second version of the largest the short one 

# number_1 = int(input("enter a number to get largest  : ".title()))
# number_2 = int(input("enter a number to get largest : ".title()))

# def largests(number_1,number_2):
#     if number_1> number_2 :
#         return number_1
#     else:
#         return number_2
 
 
# answers = largests(number_1,number_2)
# print(answers)

# creating a function to check a number is a even or odd

# number = int(input("enter a number to check whether it is even or odd : ".title()))

# def even_odd(number):

#     if number % 2 == 0 : 
#         print(f"the Number {number} is a even number".title())

#     else : 
#         print(f"The number {number} is a odd number".title())

# even_odd(number)


# # return version of previous code 

# number = int(input("enter a number to check whether it is even or odd : ".title()))

# def even_odd(number):

#     if number % 2 == 0 : 
#         return "Even"
#     else : 
#         return "Odd"

# even_odd_check = even_odd(number)
# print(even_odd_check)

# Vote eligibility check

# age = int(input("Enter your age : ".title()))

# def vote_check(age):

#     if age >= 18 : 
#         print("Congratulations You are eligible to vote".title())

#     else :
#         print("you are unable to vote".title())

# vote_check(age)

# Now the return version

# age = int(input("Enter your age : ".title()))

# def vote_check(age):

#     if age >= 18 : 
#         return "You are eligible to vote".title()

#     else :
#         return "you can't vote".title()

# vote = vote_check(age)
# print(vote)


# Now the Most difficult as of my level 
# bank Withdrawn system 

# balance = int(input("Enter Your Balance : "))
# amount = int(input("enter a amount to be withdrawn :".title()))

# def withdrawn(balance,amount):
    
#     if amount <= 0 :
#         print("Invalid Amount")
#     elif amount <= balance :
#         print(f"The Remaining balance after withdrawing {amount} is : ".title(),balance - amount)

#     elif amount > balance :
#         print("Insufficient Balance")

   

# withdrawn(balance,amount)

# # now with return 

# balance = int(input("Enter Your Balance : "))
# amount = int(input("enter a amount to be withdrawn :".title()))

# def withdrawn(balance,amount):

#     if amount <= 0 :
#         return "Invalid Amount"
#     elif amount <= balance :
#        return f"The Remaining Balance Is: {balance - amount}"

#     elif amount > balance :
#         return "Insufficient Balance"

    

# withdrawn_function = withdrawn(balance,amount)
# print(withdrawn_function)


# argument function 

def greet(name):
    print(f"Hello {name}... how are you ? ".title())

greet("dhruv")

