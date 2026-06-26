# There are two types of scopes in python :
# 1) Local Scope : 
    # Variables defined inside a function are in the local scope of that Function
    # Local Variables can only be accessed in that function only where they are defined
     
# 2) Global Scope :
    # Variables defined outside of any function are in the global scope of the module
    # Global Variables can be accessed from anywhere in the whole program

def add(a,b):
    c = a + b   # This is Local variable because it is defined inside the function
    k = 45
    print(c)

k = 98
add(97,99)

print(k)  # This will print 98, the global variable x as it is global variable as it can be accessed in whole program

# global keyword 
# global keyword is used to modify a global variable inside a function


def add_global(a,b):
    d = a+b
    global z  # This will modify the global variable z 
    z = 200  
    print(d)

z = 100 # This is a global variable
add_global(45,98)

print(z)  # This will print 200, the modified global variable z

