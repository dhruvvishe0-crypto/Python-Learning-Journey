# magic / dunder methods are also called as double underscore methods
# this methods starts with double underscore like __init__, __str__ , __repr__
# this methods allow us to define how our objects interacts with the operators,functions and etc

# some common magic methods with example :

# 1) __init__ =  we all know it's constructor

# code =

class employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

e = employee("Dhruv", 150000)

print(e.name)
print(e.salary)


'''
2) __str__ = This method should return a human-readable, informal string
              representation of the object. It's used by the str() function and by
               print also this is used to show message to the user
'''

class employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"The name of the employee is {self.name} and salary is {self.salary}".title()


e = employee("Dhruv", 150000)
print(e.__str__())


'''
3) __repr__  = This method should return an unambiguous, official string
representation of the object. Ideally, this string should be a valid Python
expression that could be used to recreate the object. It’s used by the repr()
function and in the interactive interpreter when you just type the object’s
name and press Enter  also this is used to by developer to debug mostly it is used for this

'''

class employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"The name of the employee is {self.name} and salary is {self.salary}".title()

    def __repr__(self):
        return f"name : {self.name} \nsalary : {self.salary}".title()

e = employee("Dhruv", 150000)
print(e.__str__())
print(e.__repr__())


'''
4)__len__ = This method allows objects of your class to work with the built-in len() function.
            It should return the “length” of the object (however you define that).


'''

class employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"The name of the employee is {self.name} and salary is {self.salary}".title()

    def __repr__(self):
        return f"name : {self.name} \nsalary : {self.salary}".title()

    def __len__(self):
        return len(self.name)    # if we have get the length of name

e = employee("Dhruv", 150000)
print(e.__str__())
print(e.__repr__())
print(e.__len__())

'''
4) _add__ , __sub__ , __mul__ , etc. - Operator Overloading
These methods allow you to define how your objects behave with standard
arithmetic and comparison operators.

'''

class vectors:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return vectors(self.x + other.x , self.y + other.y)

    def __sub__(self,other):
        return vectors(self.x - other.x , self.y - other.y)

    def __mul__(self,scaler):
        return vectors(self.x * scaler , self.y * scaler)

    def __str__(self):
        return f"Vector : ({self.x},{self.y})"

v1 = vectors(2,4)
v2 = vectors(3,5)
v3 = v1 + v2 # calls add
print(v3)
v4 = v3 - v1
print(v4)
v5 = v1 * 5
print(v5)

