# Day 3 Python Practice

# Question 1: Login System
"""
Objective:
Create a simple login system.

Requirements:

1. Username should be "Dhruv"
2. Password should be "python123"

If both are correct:
    Print "Login Successful"

Otherwise:
    Print "Invalid Username or Password"

Use a function.
"""


# username = str(input("Enter your username :".title()))
# password = input("Enter your password :".title())

# def login_system(username,password):

#     if username == "Dhruv" and password == "python123" :
#         print("login successful".title())

#     else :
#         print("Invalid username or password".title())

# login_system(username,password)



# Question 2: Number Guessing Game (While Loop)


"""
Objective:
Practice the while loop.

Requirements:

1. Secret number = 7
2. Ask the user to guess the number.
3. Keep asking until the correct number is entered.
4. Print "Correct Guess!" when guessed correctly.

Use a while loop.
"""


# secret_number = 7

# while True :
#     guess = int(input("Enter your guess :".title()))
#     if guess == secret_number :
#         print("correct guess".title())
#         break
#     else :
#         print("try again , wrong guess ".title())


# Question 3: Email Validator

"""
Objective:
Validate an email.

Rules:

Email must contain:

@
.

If both are present:
    Print "Valid Email"

Otherwise:
    Print "Invalid Email"

Use a function.
"""

# email = input("enter your email to check it is valid or not : ".title())

# def email_validate_checker(email):

#     if "@" in email and "."in email :
#         print("Valid email ".title())

#     else :
#         print("invalid email".title())

# email_validate_checker(email)




# Question 4: Shopping Discount


"""
Take prices of 5 products.

Store them in a list.

Calculate total bill.

Discount Rules:

Total >= 5000
20% Discount

Total >= 2000
10% Discount

Otherwise
No Discount

Print:

Total
Discount
Final Amount
"""

# product_1 = int(input("Enter the price of 1st product :".title()))
# product_2 = int(input("Enter the price of 2nd product :".title()))
# product_3 = int(input("Enter the price of 3rd product :".title()))
# product_4 = int(input("Enter the price of 4th product :".title()))
# product_5 = int(input("Enter the price of 5th product :".title()))

# price_list =[product_1,product_2,product_3,product_4,product_5]

# def shopping_discount(price_list):

#     total = sum(price_list)
#     if total >= 5000 :
#         discount = total * 0.20
#         final_amount = total -discount
#         print("total bill : ".title(),total)
#         print("discount :".title(),discount)
#         print("Final Amount :",final_amount)

#     elif total >= 2000 :
#         discount = total * 0.10
#         final_amount = total -discount
#         print("total bill : ".title(),total)
#         print("discount :".title(),discount)
#         print("Final Amount :",final_amount)

#     else :
#         print("total bill :".title(),total)
#         print("no discount applied ".title())
#         print("final amount :".title(),total)


# shopping_discount(price_list)



# Question 5: Student Attendance

"""
Attendance Percentage is entered by user.

Rules:

if attendance >=75%
Eligible for Exam

Else
Not Eligible

Use a function.
"""

# attendance = int(input("enter your attendance percentage :".title()))

# def student_attendance(attendance):

#     if attendance >= 75 :
#         print("eligible for exam".title())

#     else:
#         print("not eligible for exam".title())

# student_attendance(attendance)


# Question 6: Password Analyzer

"""
Take a password.

Print:

Length

Number of digits

Number of alphabets

Strong or Weak

Strong means:
Length >= 8
AND
Contains at least one digit.

"""

# password = input("enter a password to check its strength :".title())

# def password_checker(password) :
#     no_of_digits = 0
#     no_of_alphabets = 0

#     for i in password :
#         if i.isdigit() :
#             no_of_digits +=1
#         elif i.isalpha() :
#             no_of_alphabets += 1

#     print("the length of password is : ".title(),len(password))
#     print("number of digits this password contains :".title(),no_of_digits)
#     print("number of alphabets this password contains :".title(),no_of_alphabets)

#     if len(password) >= 8 and no_of_digits > 1 :
#         print("strong password".title())

#     else :
#         print("weak password".title())

# password_checker(password)


# Question 7: Word Analyzer

"""
Take a word.

Print:

1. Total Characters
2. Total Vowels
3. Reverse Word
4. Uppercase
5. Lowercase

Create a function.
"""

# word = str(input("enter a word :".title()))

# def word_analyzer(word):

#     print("total character in this word are :".title(),len(word))
#     count = 0
#     for i in word.lower() :
#         if i in "aeiou":
#             count = count + 1

#     print("The no. of vowels in the owrd are : ",count)
#     print("the reverse of this word is :".title(),word[::-1])
#     print("this word in uppercase is :".title(),word.upper())
#     print("this word in lowercase is :".title(),word.lower())

# word_analyzer(word)

# Question 8: Student Report Card

"""
Take:

Student Name

5 Subject Marks

Store marks in a list.

Calculate:

Total

Average

Highest Marks

Lowest Marks

Grade

Rules:

>=90 -> A
>=75 -> B
>=50 -> C
Else -> Fail
"""


subject_1 = int(input("enter your marks of maths :".title()))
subject_2= int(input("enter your marks of sanskrit :".title()))
subject_3 = int(input("enter your marks of english :".title()))
subject_4 = int(input("enter your marks of marathi:".title()))
subject_5 = int(input("enter your marks of science :".title()))

list_of_marks = [subject_1,subject_2,subject_3,subject_4,subject_5]

def student_report_card(list_of_marks):

    total = sum(list_of_marks)
    average = total /len(list_of_marks)
    highest_marks = max(list_of_marks)
    lowest_marks = min(list_of_marks)

    print("your total marks are : ".title(),total)
    print("your average marks are :".title(),average)
    print("your highest marks are :".title(),highest_marks)
    print("your lowest marks are :".title(),lowest_marks)


    if average >= 90 :
        print("Congratulations you Got grade A".title())
    elif average >= 75 :
        print("congratulations you got grade B ".title())

    elif average  >= 50 :
        print("congratulations you got grade C ".title())
    else :
        print("sorry you are failed ".title())

student_report_card(list_of_marks)



# Question 9: Library Book Search

"""
books = ["Python", "Java", "C++", "HTML", "SQL"]

Take a book name from the user.

If the book exists:

Print:
Book Available

Else:

Print:
Book Not Available
"""

# books = ["Python", "Java", "C++", "HTML", "SQL"]

# book = str(input("enter a book name to find : ".title())).title()

# def book_search(books):

#     for i in books :
#         if i == book :
#             print("book available".title())
#             break
#     else:
#          print("book not available".title())

# book_search(books)



# Question 10: List Comprehension Challenge

"""
Create a list of numbers from 1 to 30.

Store only numbers that are divisible by both 2 and 3.

Use list comprehension.

Expected Output:

[6, 12, 18, 24, 30]
"""



numbers = [i for i in range(1,31) if i % 2 == 0 and  i % 3 == 0 ]
print(numbers)