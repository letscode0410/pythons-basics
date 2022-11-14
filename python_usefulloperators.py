########################################################
#range | enumerate | zip | in |randint
########################################################

mylist=[1,2,3]

for i in range(10):
    print(i)

for i in range(1,10,2):
    print(i)

genlist=list(range(1,50,3))
print(genlist)




word ="ravi kumar"

for index,letter in enumerate(word):
    print(index," - ",letter)

mylist1 =[1,2,3]
mylist2 =['a','b','c']
#(1, 'a')
#(2, 'b')
#(3, 'c')
for item in zip(mylist1,mylist2):
    print(item)


mylist3 =[10,20,20,30,40]
#extra items will be ignored
# (1, 'a', 10)
# (2, 'b', 20)
# (3, 'c', 20)
for item in zip(mylist1,mylist2,mylist3):
    print(item)

ziplist=  list(zip(mylist1,mylist2,mylist3))
print(ziplist)
#[(1, 'a', 10), (2, 'b', 20), (3, 'c', 20)]

print('a' in 'a world')
print(2 in [3,4,5])

dict1 = {'key1':123,'key2':456}

is_key_in = 'key1' in dict1
is_key_in1 = 'key2' in dict1.keys()
is_value_in = 123 in dict1.values()

print("is_key_in",is_key_in)
print("is_key_in1",is_key_in1)
print("is_value_in",is_value_in)

from random import randint

print("randint",randint(1,200))