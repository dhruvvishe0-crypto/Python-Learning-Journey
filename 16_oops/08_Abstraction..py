# we are learning about abstraction now

# abstraction means hiding the complex details and showing the necessary functionality to the user

# for Example :  suppose you are driving a car you accelerate the car you press the break you shift the gears etc you do all of this but you dont know how the gear shifts how breaks are applied how engine works etc so this is a called abstraction where complex details / implementations are hidden and here user just interact with them

# in Python it is achieved using abstract classes and abstract methods

# now we will practice some questions

"""
You are creating an Online Payment System.

Every payment method must have a pay() method.

Create an abstract class named Payment.

Create an abstract method:
- pay()

Create two child classes:

UPI

CreditCard

Each class should implement pay() in its own way.

Create one object of each class.

Call pay().
"""


from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class UPI(Payment):
    def pay(self,pay):
        print(f"Paid successfully using UPI {pay}".title())


class CreditCard(Payment):
    def pay(self,pay):
        print(f"Paid successfully using creditcard {pay}".title())

upi = UPI()
creditcard = CreditCard()

upi.pay(299)
creditcard.pay(500)