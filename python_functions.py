func_samples='''
#########################################
########## PYTHON FUNCTIONS #############
#########################################
'''

#doesn't expect any parameter
#and doesn't return anything
def welcome_message():
    print(func_samples)

welcome_message()

#len
#max , min
list1= [1,2,8,3,4,6,59,9]
print("Maximum nubber from list : ",max(list1))
print("Minimum nubber from list : ",min(list1))
print("Sum nubber from list : ",sum(list1))

def avg_of_nums(a,b):
    count =2
    avg_results = (a+b)//2
    return avg_results

print(avg_of_nums(5,9))
print(avg_of_nums(4,9))

#factorial

def factorial(num):
    fact =1
    for i in range(1,num+1):
        fact *=i
    return fact

print(factorial(6))


#even number

def even_check(number):
    return number%2 ==0

print("is even ",even_check(5))


#optional argument, and optional arguments should always followed by non -optional arguments 
# multiply(a=3,b) not allowed
def multiply(a,b=3):
    return a*b

print(multiply(5,2))
print(multiply(6))

def multiply(a,b=3,c=1):
    return a*b*c

print(multiply(5,2,5))
print(multiply(6,2))

#Check if any number in a list is even

def check_if_even_list(num_list):
    for num in num_list:
        if(num%2==0):
            return True
        else:
            pass
    return False

print("check_if_even_list([3,5,6,7])",check_if_even_list([3,5,6,7]))
print("check_if_even_list([3,5,9,7])",check_if_even_list([3,5,9,7]))


#Return all even numbers in a list
def get_even_list(num_list):
    even_numbers=[]
    for num in num_list:
        if num%2==0:
            even_numbers.append(num)
        else:
            pass
    return even_numbers

print("get_even_list(range(1,11))",get_even_list(range(1,11)))

#The employee of the month function will return both 
# the name and number of hours worked for the top 
# performer (judged by number of hours worked).    
work_hours = [('ravi',100),('kumar',400),('reddy',800)]

def get_top_performer(work_hours):
    max_hours =0
    employee_of_month=""
    for employee,hours in work_hours:
        if hours > max_hours:
            max_hours=hours
            employee_of_month=employee
        else:
            pass
    return (employee_of_month,max_hours)

print("get_top_performer(work_hours)",get_top_performer(work_hours))


#Non-key values arguments
def  example_nonkeyed_args(*argv):
    results=0
    for param in argv:
        results+=param
    return results

print(example_nonkeyed_args(1,5,6))
print(example_nonkeyed_args(1,5))


def get_even_list(*args):
    return [x for x in args if x%2==0]

print("get_even_list(1,2,3,45,6)",get_even_list(1,2,3,45,6))
#key value type of arguments
def example_of_kwargs(**kwargs):
    for k,v in kwargs.items():
        print("key :",k," value :",v)

example_of_kwargs(host="localhost",port=9091,pswd="xxx")



def myfunc(*args, **kwargs):
    if 'fruit' and 'juice' in kwargs:
        print(f"I like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
        print(f"May I have some {kwargs['juice']} juice?")
    else:
        pass
        
myfunc('eggs','spam',fruit='cherries',juice='orange')


