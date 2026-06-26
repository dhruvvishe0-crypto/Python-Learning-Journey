#Question 1: Student Grade Calculator

#Objective:
#Create a function that takes student marks and returns the grade

#Grading Criteria:
# Marks >= 90  -> Grade A
# Marks >= 75  -> Grade B
# Marks >= 50  -> Grade C
# Otherwise    -> Fail

# Requirements:
# Take marks as input from the user.
# Create a function named grade_calculator().
# Return the grade.
# Print the returned result.

marks = int(input("Enter Your Marks : "))

def grade_calculator(marks):
    if marks >= 90 :
        print("Congratulations You Got grade a ".title())
    elif marks >= 75 :
        print("Congratulations You got grade b".title())
    elif marks >= 50 :
        print("congratulations you got grade c".title())
    else :
        print("sorry you are failed ".title())

grade_calculator(marks)


# Question 2: Multiplication Table

# Objective:

# Create a function that prints the multiplication table of a number.

# Requirements:
# Take a number as input.
# Create a function named table().
# Print the multiplication table from 1 to 10.

number = int(input("enter a number to get table of it : ".title()))

def table(number):
    for i in range(1,11):
        print(f"{number} X {i} = ", number * i)

table(number)



# Question 3: Count Vowels

# Objective:

# Count the total number of vowels in a string.

# Requirements:
# Take a string as input.
# Use a loop.
# Count vowels:
# a, e, i, o, u
# Print the total count.

word = str(input("Enter a word to get the total number of vowels in it : ".title()))

def count_vowels(word):
    count = 0
    for i in word.lower():
        if i in "aeiou":
            count = count+1
    return count

print(count_vowels(word))


# Question 4: Reverse a String

# Objective

# Reverse the string entered by the user.

# Requirements :
# Take a string as input.
# Create a function named:
# Return the reversed string.
# Print the returned value.

Word_4 = str(input("Enter a word to reverse it : ".title()))

def reverse_string(word_4):
    print(word_4[::-1])

reverse_string(Word_4)


# Question 5: Sum of List Elements

"""
Objective:
Find the total sum of all numbers in the list.

Requirements:
1. Use a loop.
2. Do NOT use sum().
3. Print the final total.

"""

numbers = [10, 20, 30, 40, 50]

def sum_of_numbers(numbers):
    total = 0
    for i in numbers:
        total = total + i
    return total
print(sum_of_numbers(numbers))



# Question 6: Shopping Bill Calculator

"""
Objective:
Calculate the final shopping bill.

Requirements:

1. Take the price of 3 products from the user.
2. Store them in a list.
3. Calculate the total bill.
4. If total bill is greater than 1000,
   give a 10% discount.
5. Print:
   - Total Bill
   - Discount
   - Final Amount
"""



product_1 = int(input("Enter Price Of Product 1: "))
product_2 = int(input("Enter Price Of Product 2: "))
product_3 = int(input("Enter Price Of Product 3: "))

list_of_prices = [product_1, product_2, product_3]

def shopping_bill(list_of_prices):

    total = 0

    for price in list_of_prices:
        total += price

    if total > 1000:

        discount = total * 0.10
        final_amount = total - discount

        print("Total Bill:", total)
        print("Discount:", discount)
        print("Final Amount:", final_amount)

    else:

        print("Total Bill:", total)
        print("No Discount Applied")
        print("Final Amount:", total)

shopping_bill(list_of_prices)



# Question 7: Username Validator

"""
Objective:
Validate a username.

Requirements:

1. Create a function named validate_username().
2. Take username input from the user.
3. If username contains 5 or more characters:
      Print "Valid Username"
4. Otherwise:
      Print "Invalid Username"


"""


username = str(input("Enter your username : ".title()))

def validate_username(username):

    length_of_username = len(username)

    if length_of_username >= 5 :
        print("valid username".title())

    else :
        print("invalid username".title())

validate_username(username)


# Question 8: Count Positive Numbers

"""
Objective:
Count the number of positive numbers in the list.

Requirements:

1. Use a loop.
2. Count only positive numbers.
3. Print the final count.

Expected Output:
3
"""

numbers = [5, -2, 8, -1, 10, -7]

def count_positive_numbers(numbers):
    count = 0
    for i in numbers:
        if i > 0:
            count += 1
    return count

print(count_positive_numbers(numbers))


# Question 9: Student Marks Analyzer

"""
Objective:
Analyze student marks.

Requirements:

1. Store marks in a list.
2. Calculate:
      - Total Marks
      - Average Marks
3. Print both.

Example:

Marks:
[80, 90, 70, 85, 75]

Output:

Total Marks: 400
Average Marks: 80
"""

subject_1 = int(input("enter your marks of maths : ".title()))
subject_2 = int(input("enter your marks of science : ".title()))
subject_3 = int(input("enter your marks of marathi : ".title()))
subject_4 = int(input("enter your marks of english: ".title()))
subject_5 = int(input("enter your marks of sanskrit: ".title()))

list_of_marks = [subject_1, subject_2, subject_3, subject_4, subject_5]

def total_marks_and_average(list_of_marks):
    total = 0
    for i in list_of_marks :
        total +=i

    average = total / len(list_of_marks)
    print("total marks :".title(),total)
    print("the average of your marks is :".title(),average)

total_marks_and_average(list_of_marks)
