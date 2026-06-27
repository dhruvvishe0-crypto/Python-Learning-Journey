# oops questions Practice i have taken this question from chatgpt


"""
Create a class named Mobile.

Attributes:
- brand
- model

Method:
- mobile_info()

Output Example:

Brand: Samsung
Model: S24
"""

class mobile :
    def  __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def mobile_info(self):
        print(f"The brand of the mobile is {self.brand} . \nthe model of the mobile is {self.model} .".title())

mobile_1 =mobile("samsung","s24")

mobile_1.mobile_info()


"""
Create a class named Book.

Attributes:
- title
- author

Method:
- display_book()

Output Example:

Book Name: Atomic Habits
Author: James Clear
"""

class book :
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def display_book(self):
        print(f"book name : {self.title} \nauthor : {self.author} ".title())


book_1 = book("the power of your subconscious mind","james clear")

book_1.display_book()


"""
Create a class named Laptop.

Attributes:
- brand
- ram
- storage

Method:
- show_specs()

Output Example:

Brand: HP
RAM: 16 GB
Storage: 512 GB
"""


class laptop :
    def __init__(self,brand,ram,storage):
        self.brand = brand
        self.ram = ram
        self.storage = storage

    def show_specs(self):
        print(f"Brand : {self.brand}  \nram : {self.ram}  \nstorage : {self.storage} ".title())

laptop_1 =laptop("Hp","16gb","512gb")
laptop_1.show_specs()


"""
Create a class named Fan.

Attribute:
- speed (initially 0)

Methods:
- increase_speed() -> increase speed by 1
- show_speed()

Example:

Initial Speed = 0

After calling increase_speed() twice

Output:

Current Speed = 2
"""


class fan :
    def __init__(self,speed = 0):
        self.speed = speed
    def increase_speed(self):
        self.speed += 1

    def show_speed(self):
        print(f"The current speed of the fan is {self.speed}".title())

fan_1 = fan()
fan_1.increase_speed()
fan_1.increase_speed()
fan_1.show_speed()


"""
Create a class named BankAccount.

Attribute:
- balance

Methods:
- deposit(amount)
- withdraw(amount)
- check_balance()

Rules:

Do not allow withdrawal if balance is insufficient.
"""


class BankAccount :
    def __init__(self,balance):
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def withdrawn(self ,amount):
        self.balance -= amount

    def check_balance(self):
        print(f"Your balance is : {self.balance}".title())

balance_1 = BankAccount(100000)
balance_1.deposit(50000)
balance_1.check_balance()
balance_1.withdrawn(2000)
balance_1.check_balance()






