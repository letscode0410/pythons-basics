
list1 = [1,3,4,2,5,6,7,12,1,31,4,15]

data = map(lambda x:"even" if x%2==0 else "odd",list1)

for i in data:
    print(i)