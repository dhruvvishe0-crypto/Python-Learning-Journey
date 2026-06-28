# Inheritance means one class can use properties and methods of another class

# suppose your father has a car ,house and land and you are his kid so you dont build new house and dont buy a car also dont buy land but you get all these things from your dad so you inherit them from your dad
# this is the concept of inheritance

# First Example :

class Animal :                     # this is a parent class or our main blueprint
    def __init__(self,name):     # We know this is a constructor and how this works
        self.name = name

    def speak(self):              # this is a method we all know this
        print("Animals Can Make Sounds")

class Dog(Animal):                   # this is a child class which is inheriting from the parent class
    pass                             # we are writing pass because we don't want to write anything in this class we have everything inherited from parent class

dog_1 =Dog("Tommy")         # we are creating an object
dog_1.speak()


"""
Create a parent class named Animal.

Inside it:

Constructor:
- name

Method:
- speak()

Print:
Animals make sounds.

Now create a child class Dog.

Do not write anything inside Dog.

Create an object:

dog_1 = Dog("Tommy")

Print the dog's name.

Call speak().
"""


class Animal :
    def __init__(self,name):
        self.name = name

    def speak(self):
        print("Animals make sounds")


class Dog(Animal):
    pass

dog_1 =Dog("Tommy")
dog_1.speak()
print(dog_1.name)


"""
Create a parent class named Vehicle.

Constructor:
- brand

Method:
- show_brand()

Print:

Brand: BMW

Now create a child class Car.

Don't write any constructor inside Car.

Create an object and call the method.
"""

class Vehicle :
    def __init__(self,brand):
        self.brand = brand

    def show_brand(self):
        print(f"Brand : {self.brand}".title())

class car(Vehicle):
    pass

car_1 = car("mercedes")
car_1.show_brand()


"""
Create a parent class named Person.

Constructor:
- name
- age

Method:
- introduce()

Output Example:

My name is Dhruv.
I am 20 years old.

Create a child class Student.

Create one object and call introduce().
"""

class Person :
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}. \nI am {self.age} years old ".title())

class student(Person):
    pass

student_1 = student("Dhruv",18)
student_1.introduce()


"""
Create a parent class named BankAccount.

Constructor:
- balance

Methods:
- deposit(amount)
- withdraw(amount)
- check_balance()

Don't allow withdrawal if balance is insufficient.

Create a child class SavingsAccount.

Create one object.

Deposit money.

Withdraw money.

Check balance.
"""
class  BankAccount :
    def __init__(self,balance):
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def withdrawn(self,amount):
        if amount > self.balance :
            print("Insufficient Balance".title())

        else :
            self.balance -= amount


    def check_balance(self):

        print(f"The balance of your account is {self.balance}".title())

class SavingsAccount(BankAccount) :   # if we remove the BankAccount from here it will stop inheriting from BankAccount so the calling of methods will not work
    pass

savings_1 = SavingsAccount(10000)
savings_1.deposit(5000)
savings_1.check_balance()
savings_1.withdrawn(16999)
savings_1.check_balance()

# This Question are too basic  i am just practising it so that in future i can understand it

# a Child class can have it's own methods for example :

class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating".title())

class Dog(Animal):

    def bark(self):
        print("woof Woof".title())   # here we can see that we can write our own methods not just one method but multiple methods



dog_1 = Dog("Tommy")
dog_1.eat()
dog_1.bark()

# now we will solve some questions


"""
Create a parent class named Person.

Constructor:
- name

Method:
- walk()

Output:
"{name} is walking."

Create a child class Student.

Inside Student create a method:

study()

Output:
"{name} is studying."

Create one Student object.

Call both methods.
"""

class student_1 :
    def __init__(self,name):
        self.name = name

    def walk(self):
        print(f"{self.name} is walking".title())

class student(student_1):
    def study(self):
        print(F"{self.name} is studying".title())

student_1 = student("Dhruv")
student_1.walk()
student_1.study()

