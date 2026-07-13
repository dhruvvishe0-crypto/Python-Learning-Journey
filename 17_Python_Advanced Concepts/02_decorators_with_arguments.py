# we have seen decorators but now we will see decorator with argument
def repeat(number):
    def decorator(func):
        def wrapper(a):
            for i in range(number):
                func(a)
        return wrapper
    return decorator
@repeat(7)
def greet(name):
    print(f"{name}")

greet("Dhruv")


# creating a decorator that checks the admin permission


def permission(role):
    def decorator(func):
        def wrapper(a):
            if role == "admin":
                print("Checking admin Permissions....")
                func(a)
            else :
                print("you do not have the permission".title())
        return wrapper
    return decorator

def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator


@permission("staff")

def delete_server(name):
    print(f"server named {name} has been deleted successfully".title())

delete_server("ZenThrox")

@permission("admin")
@repeat(3)
def change_name(name):
    print(f"You have changed the name of server to {name}")
change_name("ZenThrox_Army")






# discount
def discount(percent):
    def decorator(func):
        def wrapper(a):
            if percent <= 30 :
                print(f"Applying The Discount of {percent} ")
                func(a)
            else:
                print("Discount is not applicable")
        return wrapper
    return decorator

@discount(20)
def Percentage(item_name):
    print(f"Congratulations You have Got discount on {item_name}")

Percentage("Laptop")
@discount(45)
def Percentage(item_name):
    print(f"Congratulations You have Got discount on {item_name}")

Percentage("Laptop")

