# what is Empty class ?

# EX :

class Empty :        #class is the keyword used to create a class

    pass   # We Write pass because python doesn't allow empty class so actually pass does nothing also we can add code later

empty_class_object = Empty()   # We have created a object here

print(empty_class_object )   # this will print the object

# output will be <__main__.Empty_class object at 0x000002339F9586E0> this so when we have empty class then this will be the output



# Now learning about constructor what is it and how it works

# First we write a code

class student :     # as usual this creates a our class
    def __init__(self,name):    # this is the constructor it runs automatically whenever object is created we dont have to call it
        self.name = name                  # what is self so it basically refers to the object so in our case during execution of code python thinks self = student_1,student_2



student_1 = student("harsh")     # so here python creates a object where python secretly thinks self = student_1 so it becomes student.name = Dhruv or Harsh
student_2 = student("Dhruv")      # same thing happens for student_2


print(student_1.name)   # now it prints the output
print(student_2.name)



# multiple objects of same class

class student_4 :
    def __init__(self,name,age,surname):
        self.name = name
        self.age = age
        self.surname = surname

student_3 =student_4("Atharva",56,"Binnar")
student_6 =student_4("Akshay",19,"bhatt")
student_7 =student_4("Vardan",19,"Varak")

print(student_3.name,student_3.age,student_3.surname)
print(student_6.name,student_6.age,student_6.surname)
print(student_7.name,student_7.age,student_7.surname)

# A single class can create multiple objects think car is a class so bmw, mercedes , suzuki are objects  same blueprint but different but different blueprint

# also in the object we can have multiple attributes like name ,age ,surname as you can see in the above problem


# There are also methods in a class These are just like functions but they are inside a class
# code of class with methods :

class car:
    def __init__(self,brand,model,color):     # You know what is this a constructor which runs automatically when an object is created
        self.brand = brand
        self.model = model
        self.color = color

    def get_info(self):      # it is as same as function like def greet(name) the one we used to create but this is called a method
        print(f"The brand of the car is {self.brand} . The model of the car is {self.model} and the color of the car is {self.color} .")

car_1 =car("bmw","M3","black")    # we are creating objects here
car_2 =car("mercedes","amg","red")

car_1.get_info()  # when we call get_info() python secretly thinks self = car_1 means car_1.get_info(self)
car_2.get_info()




# So we now we know the basics of oops we can create classes and objects so now we will create a dog class

class dog :
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def dog_info(self):
        print(f"the name of the dog is {self.name} . \nthe breed of the dog is {self.breed} . ".title())


dog_1 = dog("Tommy","Golden retriver")
dog_2 = dog("harry","labrador")

dog_1.dog_info()

dog_2.dog_info()


# SO now we will create a bank balance class in which there will be a deposit function and show balance function

# let's see

class bank_account:

    def __init__(self,balance):
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount

    def check_balance(self):
        print(f"your bank balance is {self.balance} . ".title())


balance_1 = bank_account(10000)
balance_1.deposit(29999)
balance_1.check_balance()

# so here is how it works the deposit function add the amount to the balance and the check balance function print the balance

# so now we have to create a class of car whose initial speed will be 100 km/hr but after calling the method accelerate it will add 20 km/hr speed

class car :
     def __init__(self,speed):
         self.speed = speed

     def accelerate(self):
         self.speed += 20

     def check_speed(self):
         print(f"the speed of the car is {self.speed} km/hr ".title())


car_4 = car(100)
car_4.accelerate()
car_4.check_speed()

# so it works by adding the speed by 20 with the help of accelerate method

# so we successfully created a class of car whose initial speed is 100 km/hr and after calling the method accelerate it will add 20 km/hr speed


# so now we have to create a class for youtube channel which will have n number of subscriber our choice and then it adds 50 subs to that channel using a method

class youtube:
    def __init__(self,name,subs):
        self.name = name
        self.subs = subs

    def add_subs(self):
        self.subs += 50

    def check_subs(self):
        print(f"The number of subscriber the channel {self.name} has is {self.subs}".title())

channel = youtube("ZenThrox",405)
channel.add_subs()
channel.check_subs()

# done it works same like the previous bank account class


