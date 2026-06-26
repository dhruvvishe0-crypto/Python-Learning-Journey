# Practising the Question Given by Chatgpt  Todays date - 24-06-2026

# Question 1: Number Checker

"""
Take a number from the user.

Print:

Positive Number
Negative Number
Zero

Use a function.
"""

number = int(input("Enter a number to check its a positive or a negative number : ".title()))

def number_checker(number):

    if number > 0 :
        print("its a positive number ".title())

    elif number == 0 :
        print("its neither a positive or a negative number ".title())

    else :
        print("its a negative number".title())

number_checker(number)


# Question 2: Square Calculator

"""
Take a number from the user.

Create a function.

Return the square of the number.

Print the result.

"""

number_2 = int(input("Enter a number to get the square of it : ".title()))

def square_calculator(number_2):
    return "the square of {} is {}".format(number_2,number_2*number_2).title()

print(square_calculator(number_2))

# Question 3: Count Vowels

"""
Take a word from the user.

Count total vowels.

Return the count.

Print the result.

"""

word = str(input("Enter a word to get the total number of vowels in it :".title()))

def count_vowels(word):
    count = 0

    for i in word.lower():

        if i in "aeiou":
            count = count + 1

    return count
print(count_vowels(word))


# Level 2 Questions (Logic Building)

# Question 1: ATM System


"""
Balance = 5000

Ask user:

1. Check Balance
2. Deposit Money
3. Withdraw Money

Perform the operation.

Use functions.

"""


what_user_want_to_do = str(input("sir , what do you want to do ? : ".title())).lower()

balance = 5000

def atm_system(what_user_want_to_do) :
    global balance

    if what_user_want_to_do == "check balance" :
        print("your balance is ".title(), balance)

    elif what_user_want_to_do == "deposit money":
        amount  = int(input("Enter the money you want to deposite :".title()))
        balance = balance + amount
        print("after your deposit your balance is ".title(),balance)

    else :
        amount = int(input("how much money you want to withdraw: ".title()))
        balance = balance - amount
        print(f"After withdrawing {amount} your balance is {balance}  ".title())

        return balance
atm_system(what_user_want_to_do)


# Question 2: Password Strength Checker

"""
Take a password.

If length < 8:
    Weak

If length >= 8:
    Strong

Bonus:
Check if password contains a number.
"""

password = input("Enter your password to check its strength :".title())

def password_strength_checker(password):

    count = 0

    for digit in password :

        if digit.isdigit():
            count += 1

    print(f"Your password contains  {count} digit it is good for your password".title())

    if len(password) < 8:
        print("your password is weak".title())
    elif len(password) >= 8 :
        print(" Your password is strong".title())

password_strength_checker(password)


# Question 3: Shopping Cart

"""
Take prices of 5 products.

Store them in a list.

Calculate:

Total Bill

Average Product Price

Most Expensive Product

"""

product_1 = int(input("Enter the price of 1st product :".title()))
product_2 = int(input("Enter the price of 2nd product :".title()))
product_3 = int(input("Enter the price of 3rd product :".title()))
product_4 = int(input("Enter the price of 4th product :".title()))
product_5 = int(input("Enter the price of 5th product :".title()))

product_price_list =[product_1,product_2,product_3,product_4,product_5] 

def shopping_cart(product_price_list):
    total_bill = 0
    for product in  product_price_list:
        total_bill = total_bill + product
    print("The Total bill is ".title(),total_bill)

    average_of_product = total_bill /len(product_price_list)
    print("The average of product is ".title(),average_of_product)

    most_expensive_product = max(product_price_list)
    print("The most expensive product is ".title(),most_expensive_product)

shopping_cart(product_price_list)

# Question 4: Cricket Score Analyzer

"""
Store runs scored in 5 matches.

Example:

[50, 20, 75, 100, 40]

Print:

Total Runs

Average Runs

Highest Score

Lowest Score

"""

runs_match_1 =int(input("enter your runs of your 1st match :".title()))
runs_match_2 =int(input("enter your runs of your 2nd match :".title()))
runs_match_3 =int(input("enter your runs of your 3rd match :".title()))
runs_match_4 =int(input("enter your runs of your 4th match :".title()))
runs_match_5 =int(input("enter your runs of your 5th match :".title()))

runs_list = [runs_match_1,runs_match_2,runs_match_3,runs_match_4,runs_match_5]

def cricket_score_analyzer(runs_list):
    total_runs = 0
    for runs in runs_list:
        total_runs = total_runs + runs
    print("total runs you scored in 5 matches are".title(),total_runs)

    average_runs = total_runs /len(runs_list)
    print("the average runs you scored in 5 matches are".title(),average_runs)

    highest_score = max(runs_list)
    print("the highest score you scored in 5 matches are".title(),highest_score)

    lowest_score = min(runs_list)
    print("the lowest score you scored in 5 matches are".title(),lowest_score)


cricket_score_analyzer(runs_list)



# Question 5: YouTube Channel Analytics

"""
Store views of 7 videos.

Example:

[100, 200, 50, 1000, 300, 150, 600]

Print:

Total Views

Average Views

Best Performing Video

Worst Performing Video

"""


views_1 = int(input("enter your 1 st video views :".title()))
views_2 = int(input("enter your 2 nd d video views :".title()))
views_3 = int(input("enter your 3 rd video views :".title()))
views_4 = int(input("enter your 4 th video views :".title()))
views_5 = int(input("enter your 5 th  video views :".title()))
views_6 = int(input("enter your 6 th video views :".title()))
views_7 = int(input("enter your 7 th video views :".title()))

views_list = [views_1,views_2,views_3,views_4,views_5,views_6,views_7]

def youtube_analytics(views_list):
    total_views = 0
    for views in views_list:
        total_views =total_views + views
    print("total views of 7 videos are : ".title(),total_views)

    average_views = total_views / len(views_list)
    print("average views of 7 videos are :".title(),average_views)

    best_performing_video = max(views_list)
    print("the best of performing video of your channel is :".title(),best_performing_video)

    worst_performing_video = min(views_list)
    print("the worst of performing video of your channel is :".title(),worst_performing_video)

youtube_analytics(views_list)

