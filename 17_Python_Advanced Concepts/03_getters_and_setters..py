# we will learn getter and setter by writing a code so lets go bro

class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @property   # it allows us to use methods like variable it only in reading mode we can just access it . it is a simple getter method
    def first_name(self):
        l = self.name.split(" ")
        return l[0]

    @first_name.setter    # setter is used to change the content
    def first_name(self,new_name):
        l = self.name.split(" ")
        new_name = f"{new_name} {l[1]}"
        self.name = new_name



s = student("Dhruv Vishe",45)
# print(s.first_name())
# print(s.age)

# now we will see the getter and setter method so we will use the property and setter
print(s.first_name)
s.first_name = "harsh"
print(s.first_name)



# now solving some questions

'''

Question 1 - YouTube Channel

Create a class for a YouTube channel.

What we want:

Store the subscriber count privately.

Use a getter to show the current subscribers.

Use a setter to update the subscribers.

Subscribers should never become negative.

'''


# whats wrong in this program is that we cannot have two setters for one property
class YoutubeChannel:
    def __init__(self,subscriber_count):
        self.__subscriber_count = subscriber_count

    @property
    def subscriber(self):
        return self.__subscriber_count

    @subscriber.setter
    def subscriber(self,number):
        if number < self.__subscriber_count :
            self.__subscriber_count -= number
            return self.__subscriber_count
        else:
            self.__subscriber_count = 0
            return self.__subscriber_count


y = YoutubeChannel(410)
# print(y.show_subscriber())
# print(y.increase_subscriber(50))
# print(y.show_subscriber())
# print(y.decrease_subscriber(400))
# print(y.show_subscriber())
# print(y.decrease_subscriber(450))
# print(y.show_subscriber())

print(y.subscriber)
y.subscriber = 20
print(y.subscriber)


'''
🟢 Question 2 - Steam Game Price

Create a class for a Steam game.

What we want:

Store the game price privately.
Getter should return the current price.
Setter should change the price.
Price should never become less than ₹0. '''



# i have added my own features to it


class SteamGame:

    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):

        if new_price < 0:
            print("Price cannot be negative.")
        else:
            self.__price = new_price

    def increase_price(self, amount):

        if amount > 0:
            self.__price += amount
            print(f"Price increased successfully to ₹{self.__price}")
        else:
            print("Invalid amount.")

    def decrease_price(self, amount):

        if amount <= 0:
            print("Invalid amount.")

        elif amount > self.__price:
            print("Price cannot become negative.")

        else:
            self.__price -= amount
            print(f"Price decreased successfully to ₹{self.__price}")



game = SteamGame(500)

print(f"Current Price : ₹{game.price}")

choice = input("Increase or Decrease Price? ").lower()

amount = int(input("Enter Amount : "))

if choice == "increase":
    game.increase_price(amount)

elif choice == "decrease":
    game.decrease_price(amount)

else:
    print("Invalid Choice.")

print(f"Final Price : ₹{game.price}")


