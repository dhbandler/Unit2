#Daniel
#1/29/18
#fortuneTeller.py displays fortune
print("Take these colors: red and blue")

col=input("input the color of your choice ")

color=col.lower()

num=int(input("Pick a number between 1-4" ))

if color=="red" and num==1:
    print("You will get hit by an 18 wheeler and die")
    
elif color=="red" and num==2:
    print("You will be immortal")
    
elif color=="red" and num==3:
    print("You choke on a fish bone")

elif color=="red" and num==4:
    print("You die in prison")
    
elif color=="blue" and num==1:
    print("You die after you eat tainted meat")
    
elif color=="blue" and num==2:
    print("Obesity claims you")
    
elif color=="blue" and num==3:
    print("Cancer. Sorry. You have it")

else:
    print("You disappear")
    
