#how to create a class in python
class Employee:

    #constructor of the class
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    def getEmployeeDetails(self):
        return f"Name : {self.name} Salary : {self.salary}"
    
    def __str__(self) -> str:
         return f"Name : {self.name} Salary : {self.salary}"
    
    def __len__(self):
        return 1


emp = Employee("ravi",10000)
print(emp.getEmployeeDetails())
print(emp)
print(len(emp))