
list1 = [1,3,4,2,5,6,7,12,1,31,4,15]

data = map(lambda x:"even" if x%2==0 else "odd",list1)

for i in data:
    print(i)

list2 = [1,2,3,4]
list3 = [1,2,3,4]

data1= list(map(lambda x,y:x+y,list3,list2))
print(data1)



###how to use reduce####
import functools

list_x =[1,2,3,4,5,6]
res=functools.reduce(lambda x,y: x+y,list_x)
print(res)


### filter
filtered_data = filter(lambda x:x%2==0,list_x)
print(list(filtered_data))