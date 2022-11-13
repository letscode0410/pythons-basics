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
