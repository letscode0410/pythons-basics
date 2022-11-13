numbers = range(1,10)

for i in numbers:
    if i % 2 ==0:
        print(f"{i} : Even Number")
    else:
        print(f"{i} : Odd Number")

print("****************")

for letter in "Ravi Kumar":
    print(letter)

# '_' can be used when we are not using variable for loop
for _ in range(1,10):
    print("Cool!!")


#looping list of tuples
print("Looping tuples")
my_list = [(1,2),(3,4),(4,5)]

for (a,b) in my_list:
    print(a)
    print(b)


for a,b in my_list:
    print(a)
    print(b)


for x in my_list:
    print(x[0])
    print(x[1])

#looping list of dict

my_dict={'key1':'value1','key2':'value2'}

for key,value in my_dict.items():
    print(key)
    print(value)

for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)