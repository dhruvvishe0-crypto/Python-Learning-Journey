class Employee :

    company = "Microsoft"  # this is a class attribute 

    def __init__(self,name,age,salary,bond,company):
        self.name = name
        self.age = age
        self.salary = salary 
        self.bond = bond 
        self.company = company



    def get_salary(self):   
        return self.salary
    
    def get_info(self):
        print(f"the name of the employee is {self.name}. his age is {self.age}. his salary is {self.salary} and his bond is of {self.bond} ".title())

e_1= Employee("Dhruv", 18,45000,6,"Google")
print(e_1.company)  # this will always print the instance attribute whenever it is present    

print(Employee.company) # this will always print the class attribute you just have to use class name to print the class attribute


# object introspection -
# it is a method in which we use dir to get all the methods of a particular object
# ex :
print(dir(e_1))