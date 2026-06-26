# Class = Class is a Blueprint or a template Eg. suppose a form that contains the name , fathers name ,mothers name and address 

# object = object is a specific instance which is created form a class Eg. A data that contains info of john doe for a  exam form 

# creating a employee class

class Employee :

    company = "Microsoft"

    def get_salary(self):   # self is very imp here as because it is a way to reference the object of the class which is being created 
        return 34000
    
emp_1 = Employee()  # here object is created 
emp_2 = Employee()

print(emp_1.get_salary())  # here we are calling the object 
print(emp_2.get_salary())
print(emp_1.company)

