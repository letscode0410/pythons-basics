set_new = set()
print(set_new)

#how to insert values to set object
set_new.add(1)

set_new.add(2)

set_new.add(1)

set_new.add("ravi kumar")

print(set_new)

#{'r', 'a', 'k', 'u', 'v', 'm', 'i'}
set_new=set("ravikumar")
print(set_new)

#eliminates duplicates
print(set([1,1,2,3]))

#another way to declare set
set2={1,2,4}
print(type(set2)) #set

set4={}
print(type(set4)) #gives dict

lsi1=[1,2,3,4,5,6,1,2,3,4,5,6,7,8,9,3,4,56,43,11]
set5=set(lsi1)
#iteration
for item in set5:
    print(item)

list2=[3,33,44,55,2,1,3,4]
set5.update(list2)
print(set5)


### set operations

set_a={1,2,3,4,5,6}
set_b={3,6,8,9,10}

#union
print("union opeartion",set_a|set_b)

#intersection
print("Intersection operation",set_a&set_b)

#a-b difference or except
print("set_a - set_b = ",set_a-set_b)
print("set_b- set_a = ",set_b-set_a)


#compare

set_c= {1,2,3,4,5}
set_d={1,3,4,5,2,1,3,4,5}
print(set_c == set_d)
set_e=[1,2,3,4,5,6]

print(set_c==set_e)
