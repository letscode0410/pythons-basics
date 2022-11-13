x =0
while x<5:
    print(f'current value of x is {x}')
    x+=1
else:
    print(f'x value {x} is not less than 5')


for letter in "Ravi Kumar":
    if letter=='a':
        continue
    print(letter)

for letter in "Ravi Kumar":
    if letter=='a':
        break
    print(letter)

# just loop with out statement 
for letter in "Ravi Kumar":
    pass

