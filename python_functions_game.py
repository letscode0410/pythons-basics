from random import shuffle


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    guess =''
    while guess not in ['0','1','2']:
        guess = input("pick a number: 0,1 or 2")
    return int(guess)

def check_guess(mylist,guess):
    if(mylist[guess]=='0'):
        print('Correct Guess!!')
    else:
        print("wrong better luck next time")
        print(mylist)
    
# Initial List
mylist = [' ','O',' ']

# Shuffle It
mixedup_list = shuffle_list(mylist)

# Get User's Guess
guess = player_guess()

# Check User's Guess
#------------------------
# Notice how this function takes in the input 
# based on the output of other functions!
check_guess(mixedup_list,guess)