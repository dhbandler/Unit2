#Daniel Bandler
#2/12/18
#quiz2.py is our second quiz!


name1 = input("Input your first name here ")
name2 = input("Input your last name here ")

if name1>name2:
    print("Your first name is longer")
else:
    print("Your second name is longer")



if "p" in name1.lower() and "p" in name2.lower():
    print("They both have a p in them")
elif "p"in name1.lower() and "p" not in name2.lower():
    print("First name has a p. Last name does not.")
elif "p" in name2.lower() and "p" not in name1.lower():
    print("Last name has a p. First name does not.")
else:
    print("there is no p in your names")

print("You will be asked to enter two numbers that add up to 12")

num1=float(input("Input the first number here "))
num2=float(input("Input the second number here "))

if num1 + num2 == 12:
    print("Congrats! Those are valid numbers!")
else:
    print("Those numbers do not add to 10")

    
    