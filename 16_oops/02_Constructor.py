class Employee :

    def __init__(self,name,age,salary,bond):
        self.name = name
        self.age = age
        self.salary = salary 
        self.bond = bond 


    def get_salary(self):   
        return self.salary
    
    def get_info(self):
        print(f"the name of the employee is {self.name}. his age is {self.age}. his salary is {self.salary} and his bond is of {self.bond} ".title())


emp1 = Employee("Harsh",19,45000,7)
print(emp1.get_salary())
emp1.get_info()


