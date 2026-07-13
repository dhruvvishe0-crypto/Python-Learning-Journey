# Decorators are the functions that takes the function as an argument and it creates a new function inside it's body (wrapper) and then it returns the new function


def decorator(func):   # we are taking the func as an argument
    def wrapper():       # it is the new function that we created
        print("I am printing....... Hello, how are you ?  ")
        func()         # we are calling the existing function here like greet
        print("I have printed the message... Hello, how are you ? ")
    return wrapper

@decorator          # this is the main syntax everyone uses it
def greet():        # by this you make the greet function decorated for forever
    print("Hello, how are you ? ")

greet()
p= decorator(greet)   # we dont have to do this all there is also a another syntax let'go it is above the greet function
# p()

'''

the output will be
I am printing....... Hello, how are you ?
Hello, how are you ?
I have printed the message... Hello, how are you ?
'''




# practicing some questions


def decorator(function):
    def wrapper():
        print("Starting Function")
        function()
        print("Function Finished")
    return wrapper

@decorator
def greet_1():
    print("Hello Dhruv")

greet_1()


def decorator(func):
    def wrapper():
        print("Checking login .....")
        func()
    return wrapper

@decorator
def login():
    print("Opening Dashboard")

login()

def decorator(func):
    def wrapper():
        print("Function Started")
        func()
        print("Function Ended")
    return wrapper
@decorator
def download_files():
    print("Downloading Files")

download_files()


def message(func):
    def wrapper():
        print("Running Function")
        func()
        print("Finished")
    return wrapper

@message
def login():
    print("User Logged In ")
@message
def logout():
    print("User Logged Out")

login()
logout()


def decorator(func):
    def wrapper():
        print("Checking Admin Permission.....")
        func()
    return wrapper


@decorator
def deleting():
    print("Deleting Channel")

deleting()



def decorator(func):
    def wrapper():
        print("checking all The Parts of laptop")
        func()
        print("Successfully Performed the action")
    return wrapper

@decorator
def boot():
    print("Booting up laptop")
@decorator
def shutdown():
    print("shuting Down the Laptop")

boot()
shutdown()




def decorator(func):

    def wrapper():

        print("Before 1")

        func()

        print("After 1")

    return wrapper


def decorator2(func):

    def wrapper():

        print("Before 2")

        func()

        print("After 2")

    return wrapper


@decorator
@decorator2
def greet():

    print("Hello")


greet()


# python reads decorators from top to bottom



def decorator(func):
    def wrapper():
        print("Starting")
        func()
        print("Ended")
    return wrapper

@decorator
def hello():
    print("Hello Dhruv")

hello()