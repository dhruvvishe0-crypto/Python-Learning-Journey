#1. User input is used to take the input from the user at runtime.
#2.The input() function is used to take input from the user.


# Name = input("Enter your name : ")
# print(Name)

# Age = input("enter your age : ")
# print(Age)

# Mobile_Number = input("Enter Your Mobile Number :")
# print(Mobile_Number)

# Email = input("Enter Your Email : ")
# print(Email)

# print(f"Hello",Name,"I am Glad To see you You Are Still young as your age is just",Age,"Check Your mobile number is right or wrong if wrong then type again This is your Number ",Mobile_Number,"ALso check your Email Your Email:", Email)

name = str(input("Enter Your Name :"))
age = input("Enter Your Age :")
sirname = str(input("Enter Your Sirname :"))
email = input("Enter Your Email To Verify : ")

print(f"Hey,{name}, Your Age is {age} Right,And Can You confirm your Sirname is this is it {sirname} am i right,and sir your email can you verify it{email}")
confirm = str(input("if this all information is correct then type yes there : "))

print("your all info is correct congrugulations ")
