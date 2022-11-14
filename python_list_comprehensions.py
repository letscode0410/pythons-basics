############################################################################
#######                    LIST COMPREHENSIONS                  ############
############################################################################
mystring="Hello World"

mylist =[]

# for loop way to do it
for letter in mystring:
    mylist.append(letter)


#comprehensive way to do
mylist = [letter for letter in mystring]

print(mylist)

# create list number till 10
mylist =[x for x in range(0,11)]
print(mylist)

#print squres of number till number 10

my_squre_list =[x**2 for x in range(1,11)]
print(my_squre_list)

#get even numbers from 1 to 10

evennumbers= [x for x in range(1,11) if x%2==0]
print(evennumbers)

#convert celcius to fahrenheit
celcius =[0,10,20,34,6,80]
fahrenheit = [((9/5)*temp+32) for temp in celcius]
print(fahrenheit)

# if else in list comprehension is bit different than just if condition

results = ["even" if x%2==0 else "odd" for x in range(1,11)]
print(results)

################################### Nested Loops #########################################

mylist_nested = []

for i in [2,3,4]:
    for j in [100,200,300]:
        mylist_nested.append(i*j)

print(mylist_nested)


mylist_nested = [x*y for x in [2,3,4] for y in [100,200,300]]
print(mylist_nested)