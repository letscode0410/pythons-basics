#how to create a class in python
class Employee:

    count =0

    #constructor of the class
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.count +=1
    
    def getEmployeeDetails(self):
        return f"Name : {self.name} Salary : {self.salary}"
    
    def __str__(self) -> str:
         return f"Name : {self.name} Salary : {self.salary}"
    
    def __len__(self):
        return 1


emp = Employee("ravi",10000)
print(emp.getEmployeeDetails())
print(emp)
#print(len(emp))

emp1 = Employee("ravi",10000)
print(emp1.count)