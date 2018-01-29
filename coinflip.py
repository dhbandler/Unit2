#Daniel
#1/29/18
#coinFlip.py flips a coun

from random import randint

flip=input("Type 'flip' to flip the coin  ")

rand=randint(1,2)

if flip=="flip":
    
    if rand==1:
        print("Heads")
        
    elif rand==2:
        print("Tails")
        
else:
    print("Coin flip failed. You should work on your typing.")
    exit