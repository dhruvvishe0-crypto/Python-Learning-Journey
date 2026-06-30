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

# Method Overriding is a feature in inheritance where child class can override the parent class method of the same name 

# for example :

class Animal :

    def speak(self):
        print("Animals make sounds".title())

class Dog(Animal):        # so we use method overriding because dog dont say animals make sounds it says woof woof so we can override it
    def speak(self):          # here we can see that we have created a method as same name as parent class method
        print("Woof Woof")

dog_1 = Dog()
dog_1.speak()      # Python first check in dog class so it founds the speak method in dog class so it dont go to parent class ignore my english

# Most important thing to remember is that if we have same named methods in parent and child class then python goes to child class first



# Now we will practice some questions on it

"""
Create a parent class named Vehicle.

Method:
- start()

Print:
"Vehicle is starting."

Create a child class named Car.

Override the start() method.

Print:
"Car is starting."

Create one Car object.

Call start().
"""

class Vehicle :

    def start(self):
        print("Vehicle is starting".title())

class car (Vehicle):
    def start(self):
        print("car is staring".title())

car_1 = car()
car_1.start()



"""
Create a parent class named Bird.

Method:
- sound()

Print:
"Bird makes sound."

Create two child classes:

Parrot
Crow

Override sound() in both classes.

Parrot should print:
"Parrot says Hello!"

Crow should print:
"Crow says Caw Caw!"

Create one object of each class.

Call sound() using both objects.
"""


class Bird :
    def sound(self):
        print("birds make sound".title())

class parrot(Bird):
    def sound(self):
        print("parrot says hello".title())

class crow(Bird):
    def sound(self):
        print("Crow says caw caw".title())

parrot_1 =parrot()
crow_1 = crow()

parrot_1.sound()
crow_1.sound()


"""
Create a parent class named GameCharacter.

Method:
- attack()

Print:
"Character attacks."

Create three child classes:

Warrior
Archer
Wizard

Override attack() in each class.

Warrior:
"Warrior attacks with a Sword."

Archer:
"Archer attacks with a Bow."

Wizard:
"Wizard attacks with Magic."

Create one object of each class.

Call attack() using all three objects.
"""

class GameCharacter :
    def attack(self):
        print("Character attacks".title())

class Warrior(GameCharacter):
    def attack(self):
        print("warrior attacks with a sword".title())

class Archer(GameCharacter):
    def attack(self):
        print("archer attacks with a bow ".title())

class  Wizard(GameCharacter):
    def attack(self):
        print("Wizard attacks with Magic".title())


warrior_1 = Warrior()
archer_1 = Archer()
wizard_1 = Wizard()

warrior_1.attack()
archer_1.attack()
wizard_1.attack()


# Now we will learn what is super keyword

class animal:
    def __init__(self,name):
        self.name =name

    def eat(self):
        print(f"{self.name} is eating ".title())

class dog(animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed


# we will practice some question on it i mean in super keyword
'''
Question 1

Create a parent class named Animal.

Create a constructor that prints "Animal Constructor Called".

Create a child class named Dog.

Use super() to call the parent's constructor.
Then print "Dog Constructor Called".

Finally, create an object of the Dog class.
'''

class animal :
    def __init__(self):
        print("Animal Constructor called".title())

class dog(animal):
    def __init__(self):
        super().__init__()
        print("dog constructor called".title())

dog_2 = dog()





"""
Create a parent class named Person.

Constructor:
- name
- age

Create a child class named Student.

Student should have one extra attribute:
- college

Use super() to initialize name and age.

Create one object.

Print:
Name
Age
College
"""

class Person :
    def __init__(self,name,age):
        self.name = name
        self.age = age

class student(Person):
    def __init__(self,name,age,college):
        super().__init__(name,age)
        self.college = college

student_1 = student("Dhruv",18,"GPM")

print("name :".title(),student_1.name)
print("age :".title(),student_1.age)
print("college :".title(),student_1.college)


# there are total 5 types of inheritance :

# 1 ) Single Inheritance :  In single inheritance a parent class have a single child class


# 2 ) Multilevel inheritance :in multilevel indexing child class have a  child class means a parent class have grandchild class
'''
for example :

class animal:   # this is a parent class
    pass
class dog(animal):  # this is a child class
    pass
class puppy(dog):  # this is a grandchild class
    pass


# I think that's enough for today
'''

# 3 ) multiple inheritance : in this a child have 2 parents for example :

class father :
    pass
class mother :
    pass

class child(father,mother):  # this child class has 2 parents
    pass

# 4 ) Hierarchical inheritance : in this a parent class have multiple children

class animal:
    pass
class dog(animal):
    pass
class cat(animal):
    pass
class cow(animal):
    pass

# 5 ) hybrid inheritance : it is the combination of two or more types of inheritance

