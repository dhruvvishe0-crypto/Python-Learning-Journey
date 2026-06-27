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


book_1 = book("the power of your subconscious mind","joseph murphy")

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




"""
Create a class named YouTubeChannel.

Attributes:
- channel_name
- subscribers

Methods:
- gain_subscribers(number)
- lose_subscribers(number)
- show_channel()

Example:

ZenThrox

Subscribers: 500

Gain 100

Lose 50

Final:

Subscribers: 550
"""


class YoutubeChannel :
    def __init__(self,channel_name,subscribers):
        self.channel_name = channel_name
        self.subscribers = subscribers

    def gain_subscribers(self,number):
        self.subscribers += number

    def lose_subscribers(self,number):
        self.subscribers -= number

    def show_channel(self):
        print(f"channel name is {self.channel_name} \nnumbers of subscribers this channel has are {self.subscribers} ".title())

yt_channel = YoutubeChannel("ZenThrox",500)
yt_channel.gain_subscribers(100)
yt_channel.show_channel()
yt_channel.lose_subscribers(89)
yt_channel.show_channel()



"""
Create a class named Student.

Attributes:
- name
- marks (list)

Methods:

- total_marks()

- average_marks()

- show_result()

Output:

Name: Dhruv

Total: 425

Average: 85
"""

Marks = [80,87,99,89,97]

class Student :
    def __init__(self,name,marks = Marks):
        self.name =name
        self.marks = marks

    def total_marks(self):
        return sum(self.marks)
    def average_marks(self):
        return sum(self.marks) /len(self.marks)
    def show_result(self):
        print(f"name: {self.name} \ntotal: {self.total_marks()} \naverage: {self.average_marks()}".title())

student_1= Student("Dhruv")
student_1.show_result()



"""
Create a class named Employee.

Attributes:
- name
- salary

Methods:

- increase_salary(amount)

- show_details()

Example:

Salary = 40000

Increase by 5000

Output:

45000
"""
class Employee :
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def increase_salary(self,amount):
        self.salary += amount

    def show_details(self):
        print(f"salary of {self.name} is {self.salary} ".title())

Employee_1 =Employee("Harsh",40000)
Employee_1.increase_salary(14000)
Employee_1.show_details()


"""
Create a class named Car.

Attributes:

brand

speed

Methods:

accelerate()

brake()

show_speed()

Rules:

accelerate() adds 20

brake() subtracts 20

Speed should never become negative.
"""

class car :
    def __init__(self,brand ,speed ):
        self.brand = brand
        self.speed = speed

    def accelerate(self):
        self.speed += 20

    def brake(self):

        if self.speed >= 20 :
            self.speed -= 20
        else:
            self.speed = 0

    def show_speed(self):
        print(f"the speed of the car is {self.speed} km/hr and the car is of {self.brand} brand ".title())

car_1 =car("BMW",20)
car_2 =car("mercedes",0)
car_1.accelerate()
car_1.show_speed()
car_2.brake()
car_2.show_speed()


