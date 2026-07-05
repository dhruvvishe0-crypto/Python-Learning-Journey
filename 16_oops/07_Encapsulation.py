# Now we learning about encapsulation the third pillar of oops

# Encapsulation means wrapping data (attributes) and methods together inside a class and controlling how the data is accessed

# Encapsulation is used to protect important data
# and gives controlled access to it using methods.

# How Encapsulation Works

# Suppose we have a BankAccount class.

# The balance is a private variable (__balance).

# Since it is private, no one can access or modify it directly.

# Instead, we create methods like deposit(), withdraw(),
# get_balance() and set_balance().

# The user interacts with these methods instead of changing
# the variable directly.

# Example:

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance   # Private Variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount(5000)

account.deposit(1000)

print(account.get_balance())

# Output:
# 6000

# Here the user cannot do:
# account.__balance = 100000

# Instead the user uses methods provided by the class.

# This is how encapsulation works.

# It hides important data and gives controlled access to it
# through methods.

# There are three main types of encapsulation in python

'''
!) public members
2) Protected members
3) Private members

1) Public members means the data and methods can be accessed from anywhere.

2) in Protected members  variable starts with _ (underscore) Although Python allows us to access protected members, we use a single underscore (_) to tell other programmers that this variable is meant for internal use and should not be accessed directly unless necessary.
For Eg;

class Student:

    def __init__(self, name):
        self._name = name

student = Student("Dhruv")

print(student._name) # it will still print the name because python allows it

3) in Private members a variable starts with the double underscore (__) in this we cannot access the data if we try to we will get attribute error as python don't allow it
We can access the data by using getter method and also we can modify the data by using setter method

For Eg;

getter method :

class Student:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

student = Student("Dhruv")

print(student.get_name())

Getter Method:
Used to read or access a private variable.




setter method :

class Student:

    def __init__(self, name):
        self.__name = name

    def set_name(self, new_name):
        self.__name = new_name

    def get_name(self):
        return self.__name

student = Student("Dhruv")

student.set_name("Harsh")

print(student.get_name())

Setter Method:
Used to modify or update a private variable.

This are some imp types of encapsulation

'''



# Now we will practice some questions on it not too much but little bit



"""
You are creating an Instagram application.

Every Instagram account has a follower count.

The follower count should be private because nobody should
be able to change it directly.

What we want:

1. Create an Instagram account with 500 followers.

2. We should be able to see the current followers.

3. If the account gains followers,
   we should increase the follower count.

4. If the account loses followers,
   we should decrease the follower count.

5. Followers should never become negative.

Finally print the current followers.
"""

class InstagramAccount :
    def __init__(self,follower):
        self.__follower= follower

    def gain_follower(self,number):
        self.__follower += number

    def lose_follower(self,number):
        if number < self.__follower :
            self.__follower -= number

        else :
            print("this account do not have that much followers")


    def get_follower(self):

        return self.__follower


followers_of_insta = InstagramAccount(500)
follower_increase = followers_of_insta.gain_follower(100)
follower_decrease = followers_of_insta.lose_follower(657)
print(followers_of_insta.get_follower())


"""
You are creating Steam Wallet.

Every user has money in their wallet.

The wallet balance should be private.

What we want:

1. Create a wallet with ₹2000.

2. Add ₹1000 to the wallet.

3. Buy a game worth ₹1500.

4. If there isn't enough money,
   print "Insufficient Balance".

5. Finally show how much money is left.
"""

class SteamWallet :
    def __init__(self,balance):
        self.__balance = balance

    def add_money(self,amount):
        self.__balance += amount

    def buy_game(self,worth):
        if worth > self.__balance :
            print("insufficient balance".title())

        else :

            self.__balance -= worth
            print('you have successfully bought the game'.title())

    def check_balance(self):
        return self.__balance

wallet = SteamWallet(2000)
deposit = wallet.add_money(1000)
game_buy = wallet.buy_game(1500)
print(wallet.check_balance())


"""
You are creating software for a laptop.

The battery percentage should be private.

What we want:

1. Start with 80% battery.

2. Charge the laptop by 30%.

3. Battery should never go above 100%.

4. Use the laptop for some time.

5. Every hour should reduce the battery by 10%.

6. Battery should never become negative.

Finally show the battery percentage.
"""

class LaptopSoftware:
    def __init__(self,battery_percentage):
        self.__battery_percentage = battery_percentage


    def charge_battery(self,hour):

        self.__battery_percentage += hour * 10
        if self.__battery_percentage >= 100:
            self.__battery_percentage = 100
            print("Your Battery Is Full ")
        else:
            print(f"your battery is {self.__battery_percentage}".title())

    def battery_draining(self,hour):
        self.__battery_percentage -= hour * 10

        if self.__battery_percentage < 0 :
            self.__battery_percentage = 0
            print("your laptop is switched off")
    def check_battery_percentage(self):
            return self.__battery_percentage

laptop = LaptopSoftware(90)
c = laptop.charge_battery(1)
drain = laptop.battery_draining(4)
print(laptop.check_battery_percentage())



"""
You are creating a Minecraft game.

The player's health should be private.

What we want:

1. Start with 100 health.

2. Take 30 damage.

3. Heal by 20.

4. Health should never go above 100.

5. Health should never become below 0.

Finally show the current health.
"""

class Minecraft :
    def __init__(self,health):
        self.__health = health

    def damage(self,hits):
        self.__health -= hits * 10
        if self.__health <= 0 :
            self.__health = 0
            print("You are Dead")
        else :
            print(f"Your health is {self.__health}".title())

    def heal(self,eat):
        self.__health += eat*10
        if self.__health >= 100:
            self.__health = 100
            print("Your health is full".title())
        else :
            print(f"your health is {self.__health}".title())

    def show_health(self):
        return self.__health

player = Minecraft(100)
player.damage(10)
print(player.show_health())
player.heal(5)
print(player.show_health())


