#Daniel
#1/2/18
#coumpoundDemo.py how to use and/or

num=int(input("input a number "))

if num > 0 and num%7==0:
    print(num, "is positive and divisible by 7")
elif num > 0:
    print(num, "is positive and not divisible by 7")
elif num <0 and num%7==0:
    print(num, "is negative and divisible by 7")
elif num <0:
    print(num, "is negative and not divisible by 7")
else:
    print(num, "is zero")
