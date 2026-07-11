"""
You are creating a Netflix application.

Every account should have:

- Username
- Private subscription plan

What we want:

1. Create an account with the "Basic" plan.

2. Show the current plan.

3. Upgrade the plan to "Premium".

4. Show the updated plan.

The subscription plan should not be changed directly.
"""

class Netflix :
    def __init__(self,username,subscription_Plan):
        self.username = username
        self.__subscription_Plan = subscription_Plan

    def current_plan(self):
        return self.__subscription_Plan

    def upgrade_plan(self,new_plan):
        valid_plans = ["Basic","Standard","Premium","basic","standard","premium"]
        if new_plan in valid_plans :
            self.__subscription_Plan = new_plan
            print(f"You have successfully upgraded to {new_plan} Plan".title())
        else :
            print("Invalid Subscription Plan")


account = Netflix("Dhruv","Basic")
print(account.current_plan())
account.upgrade_plan("Premium")
print(account.current_plan())



"""
You are creating a Bank Locker System.

Every locker has a private password.

What we want:

1. Create a locker with a password.

2. Unlock the locker using the correct password.

3. If the password is wrong, print "Access Denied".

4. Allow changing the password only after entering the correct old password.
"""



class BankLocker :
    def __init__(self, bank_account_number, password ):
        self.__bank_account_number = bank_account_number
        self.__password = password

    def unlock_locker(self,Password):
        if self.__password == Password :
            print(f"You have successfully unlocked the locker of bank account no. {self.__bank_account_number}".title())

        else :
            print("access denied".title())

    def change_password(self, old_password ,new_password):
        if self.__password == old_password :
            self.__password = new_password
            print("you have changed your password".title())

        else :
            print("Incorrect old password. Password could not be changed.")

locker = BankLocker(23456,987654321)
locker.unlock_locker(98765432)
locker.change_password(987654321,87654321)
locker.unlock_locker(87654321)



"""
Create a parent class named Player.

Every player should have a name.

Every player should have a method:

attack()

Do not write any attack logic in the parent class.

Create three child classes:

Sniper
Assaulter
Medic

Each class should attack in its own way.

Finally create one object of each class and call attack().
"""

from abc import ABC , abstractmethod
class Player(ABC) :
    def __init__(self,name):
        self.name = name
    @abstractmethod
    def attack(self):
        pass

class Sniper(Player) :
    def attack(self):
        print(f"{self.name} attacks from a long distance as he is a sniper".title())

class Assaulter(Player):
    def attack(self):
        print(f"{self.name} attacks from close range as an assaulter.")

class Medic(Player):
    def attack(self):
        print(f"{self.name} attacks with a syringe!")
sniper =Sniper("henry")
assaulter =Assaulter("steve")
medic = Medic("Dustin")

sniper.attack()
assaulter.attack()
medic.attack()


"""
Create an abstract class named Vehicle.

Every vehicle should have a method:

rent()

Create three child classes:

Car
Bike
Truck

Each class should print its own rent message.

Example:

Car rented for ₹1500/day
Bike rented for ₹500/day
Truck rented for ₹3500/day
"""


from abc import ABC , abstractmethod
class Vehicle(ABC):

    @abstractmethod
    def rent(self):
        pass

class Car(Vehicle):
    def rent(self):
        print("Car rented for 1500/day")

class Bike(Vehicle):
    def rent(self):
        print("Bike Rented for 500/day")

class Truck(Vehicle):
    def rent(self):
        print("Truck Rented for 3500/day")


car = Car()
bike = Bike()
truck = Truck()
car.rent()
bike.rent()
truck.rent()



"""
Create a parent class named Creator.

Every creator has:

- Name
- Subscribers

Create a child class named GamingCreator.

GamingCreator should also have:

- Main Game

Use super() to initialize the common information.

Create one object and display all the information.
"""

class Creator :
    def __init__(self,name,subscribers):
        self.name =name
        self.subscribers = subscribers

class GamingCreator(Creator):
    def __init__(self,name,subscribers,main_game):
        super().__init__(name,subscribers)
        self.main_game = main_game


    def show_info(self):
        print(f"Channel Name : {self.name}")
        print(f"Subscribers : {self.subscribers}")
        print(f"Main Game : {self.main_game}")

youtube = GamingCreator("ZenThrox",406,"Minecraft")
youtube.show_info()

"""
You are creating an Amazon order system.

Every order should have:

- Private total amount

What we want:

1. Create an order worth ₹2500.

2. Add another product worth ₹500.

3. Remove a product worth ₹700.

4. Total amount should never become negative.

5. Finally show the total bill.
"""

class Amazon_Order_System:

    def __init__(self,total_amount):
        self.__total_amount = total_amount

    def add(self,amount):
        self.__total_amount += amount

    def remove(self,amount):
        if amount > self.__total_amount:
            self.__total_amount = 0
        else:
            self.__total_amount -= amount
    def show_bill(self):
        print(f"Your Total Bill Is {self.__total_amount} Rupees ")

amazon_order_system = Amazon_Order_System(2500)
amazon_order_system.add(500)
amazon_order_system.show_bill()
amazon_order_system.remove(3001)
amazon_order_system.show_bill()
amazon_order_system.add(1000)
amazon_order_system.remove(700)
amazon_order_system.show_bill()


"""
Create an abstract class named MusicPlayer.

Every music player must have:

play_song()

Create child classes:

Spotify
YouTubeMusic
AppleMusic

Each class should play the song in its own way.

Create one object of each class and call play_song().
"""
from abc import ABC ,abstractmethod

class MusicPlayer(ABC):
    @abstractmethod
    def play_song(self):
        pass



class Spotify(MusicPlayer):
    def play_song(self):
        print("Watch an ad first to listen to the song.")

class YoutubeMusic(MusicPlayer):
    def play_song(self):
        print("Enjoy listening to songs for free!")

class AppleMusic(MusicPlayer):
    def play_song(self):
        print("Buy a subscription to listen to songs.")


spotify = Spotify()
YoutubeMusicPlayer = YoutubeMusic()
AppleMusicplayer = AppleMusic()

spotify.play_song()
YoutubeMusicPlayer.play_song()
AppleMusicplayer.play_song()


"""
Create a parent class named Course.

Every course has:

- Course Name
- Instructor

Create a child class named PythonCourse.

PythonCourse should also have:

- Duration

Use super() to initialize the common information.

Display all the course details.
"""


class Course:
    def __init__(self, Course_name, Instructor):
        self.Course_name = Course_name
        self.Instructor = Instructor

class PythonCourse(Course):
    def __init__(self,Course_name,Instructor,Duration):
        super().__init__(Course_name,Instructor)
        self.Duration = Duration

    def display(self):
        print(f"Course Name : {self.Course_name}")
        print(f"Instructor : {self.Instructor}")
        print(f"Duration : {self.Duration}")

course = PythonCourse("Python","Code With Bro","6 Months")
course.display()



"""
Create a Movie Ticket Booking System.

Requirements:

1. Create an abstract class named MovieTicket.

2. Every ticket must have a method:
   book_ticket()

3. Create two child classes:

RegularTicket
VIPTicket

Each should book tickets differently.

Also keep the ticket price private.

What we want:

- Show ticket price.
- Allow changing the ticket price only through a method.
- Book the ticket.
- Print all details.
"""


from abc import ABC, abstractmethod


class MovieTicket(ABC):

    def __init__(self, price):
        self.price = price

    def show_ticket_price(self):
        print(f"Ticket Price: ₹{self.price}")

    def payment(self):
        amount = int(input("Enter payment amount: "))
        return amount

    @abstractmethod
    def book_ticket(self):
        pass


class RegularTicket(MovieTicket):

    def __init__(self):
        super().__init__(500)

    def book_ticket(self):

        payment = self.payment()

        if payment == 0:
            print(f"First pay ₹{self.price}.")

        elif payment < self.price:

            remaining = self.price - payment

            print(f"You still need to pay ₹{remaining}.")

            extra = int(input("Enter remaining payment: "))

            payment += extra

            if payment >= self.price:
                print("Ticket Booked Successfully!")
            else:
                print("Booking Failed. Full payment not received.")

        elif payment == self.price:
            print("Ticket Booked Successfully!")

        else:
            refund = payment - self.price
            print("Ticket Booked Successfully!")
            print(f"Refund Amount: ₹{refund}")


class VipTicket(MovieTicket):

    def __init__(self):
        super().__init__(1499)

    def book_ticket(self):

        payment = self.payment()

        if payment == 0:
            print(f"First pay ₹{self.price}.")

        elif payment < self.price:

            remaining = self.price - payment

            print(f"You still need to pay ₹{remaining}.")

            extra = int(input("Enter remaining payment: "))

            payment += extra

            if payment >= self.price:
                print("VIP Ticket Booked Successfully!")
            else:
                print("Booking Failed. Full payment not received.")

        elif payment == self.price:
            print("VIP Ticket Booked Successfully!")

        else:
            refund = payment - self.price
            print("VIP Ticket Booked Successfully!")
            print(f"Refund Amount: ₹{refund}")


regular = RegularTicket()

regular.show_ticket_price()

regular.book_ticket()


print("\n---------------------------\n")


vip = VipTicket()

vip.show_ticket_price()

vip.book_ticket()