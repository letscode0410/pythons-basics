my_dict={}
print(type(my_dict))

my_dict={'key1':'value1','key2':'value2'}

print(my_dict)
print(my_dict['key1'])

price_lookup = {'apple':2.99,'mango':56.98,'milk':45.6}

print(price_lookup)
print(price_lookup['milk'])

d= {'k1':123,'k2':[1,2,3],'k3':{'insideK3':109}}

print(d)

print(d['k3']['insideK3'])

print(d['k2'][2])

print(d.keys())
print(d.values())
print(d.items())

#***************************************************
print("**"*30)


person_dict={}

person_dict["name"]="Ravi Kumar"
person_dict["age"]=30
person_dict["skills"] = ["python","scala","spark","sql"]

print(person_dict)
person_dict["skills"].append("AWS")
print(person_dict["skills"])

person_dict["age"]=25

#how to get keys from a dictionary
total_keys=list(person_dict.keys())
print("Total keys: ",total_keys)

for k,v in person_dict.items():
    print("key is :",k," and value is :",v)

print('''
########################################
#  COMPARE DICTIONARY
#########################################
''')

dict3 = {'a':1,"b":4,"c":9}
dict4={'b':4,'c':9,'a':1}
print(dict3==dict4)

#how to delete specific key value pair from dictionary
print('''
how to delete specific key value pair from dictionary
''')

print(dict3)

del dict3['a']

print(dict3)

#how to check whether key presents in the dictionary

print('b' in dict3.keys())

print(type(dict3.keys()))