#Daniel
#1/19/18
#unitConverter.py converts units
print("Do you want to convert:")
print("1. Kilometers to Miles")
print("2. Kilograms to Pounds")
print("3. Liters to Gallons")
print("4. Celsius to Fahrenheit")
choi=int(input("Type the number that corresponds with the type of conversion you want to do "))

if choi == 1:
    km=float(input("Input how many km you want to convert "))
    print(km*0.621371, "miles")
    
elif choi == 2: 
    kg=float(input("Input how many kg you want to convert "))
    print(kg*2.20462, "lbs")

elif choi == 3:
    li=float(input("Input how many litres you want to convert "))
    print(li*0.264172, "gallons")
    
elif choi == 4:
    cel=float(input("Input how many degrees in Celsius you want to convert "))
    print(cel*(9/5)+32, "degrees F")

else:
    print(" How hard is it to type an ineger between 1 and 4 you silly piece of Broccoli?")
