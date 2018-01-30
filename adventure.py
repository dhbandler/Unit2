#Daniel
#1/29/18
#adventure.py make an adventure game

name=input("What is your name? ")

answ1=input("Hello there. You are lying in bed, do you get up? (y/n)")

if answ1== "y":
    answ2=input("You get out of bed and go to a dark and spooky cave. Do you go in? (y/n)")
    
    if answ2=="y":
       
        answ3=input("You enter the spooky cave, and you feel a dark, foul blast of air against your face. Do you continue, or leave? (y/n)")
        if answ3=="y":
            answ4=input("You continue, and hear heavy breathing. Do you check it out? (y/n)")
            if answ4=="y":
                print("You get gobbled up by a scary monster. How did you not see this coming,? I thought you were smarter than this")
            elif answ4=="n":
                print("Well, you waited until the last minute. Congrats on surviving, and not being eaten!")
            else:
                print("Well since you couldn't make up your mind, you just stood there like an idiot until a rock fell from the ceilling of the cave and clove your skull in two")
            
        elif answ3=="n":
            print("You leave the cave and survive. Congrats, you are not dumb")
            
        else:
             print("Clearly you can't type, so you obviously are brain damaged and stuck in a hospital and simply hallucinating all of this. Sorry.")
    elif answ2=="n":
        print("Thanks to your good judgement, you survive to another day. Congrats!")
        
    else:
        print("Clearly you can't type, so you obviously are brain damaged and stuck in a hospital and simply hallucinating all of this. Sorry.")
    
    
elif answ1=="n":
    print("By being lazy, you made the right choice, and survived. Congrats!")
    exit
    
else:
    print("Clearly you can't type, so you obviously are brain damaged and stuck in a hospital and simply hallucinating all of this. Sorry.")

