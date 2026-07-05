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