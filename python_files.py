file_data=open("sample.txt")
data=file_data.read()
print(data)

#nothing will be read
data=file_data.read()
print(data)

# now it will read
file_data.seek(0)
data=file_data.read()
print(data)

file_data.seek(0)
print(file_data.readlines())

file_data.close()

print("**************separator****************")
with open("sample.txt") as sample_file:
    print(sample_file.readlines())
    #no need to close

with open("sample.txt",mode='a') as f:
    f.write("\nfifth line by write")

with open("sample.txt",mode='r') as sample_file:
    print(sample_file.readlines())

#r = read w=write (overwrite) a= append  r+ and w+


#Basic Practice:

#http://codingbat.com/python

#More Mathematical (and Harder) Practice:

#https://projecteuler.net/archives

#List of Practice Problems:

#http://www.codeabbey.com/index/task_list

#A SubReddit Devoted to Daily Practice Problems:

#https://www.reddit.com/r/dailyprogrammer

#A very tricky website with very few hints and touch problems (Not for beginners but still interesting)

#http://www.pythonchallenge.com/