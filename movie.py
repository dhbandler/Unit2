#Daniel
#1/29/18
#movie.py prints most scandalous movie legal per age

age=float(input("What is your age? "))

if age<13:
    print("You can watch either G or PG movies. The MPAA doesn't discriminate due to age in this category.")

elif 13<=age<17:
    print("Watch PG-13 movies! The MPAA says you can watch this category when you are younger as long as you exercize caution. The MPAA also says you can watch R rated movies with parental guidance")
    
else:
    print("YOu can now watch NC-17 movies and R rated movies alone in theaters. Congrats?")
    
