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

print(factorial(6))\


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

#Non-key values arguments
def  example_nonkeyed_args(*argv):
    results=0
    for param in argv:
        results+=param
    return results

print(example_nonkeyed_args(1,5,6))
print(example_nonkeyed_args(1,5))


#key value type of arguments
def example_of_kwargs(**kwargs):
    for k,v in kwargs.items():
        print("key :",k," value :",v)

example_of_kwargs(host="localhost",port=9091,pswd="xxx")


