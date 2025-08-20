# 9. WAP to check whether a year is a leap year or not.
year=int(input("Enter year: "))
if year%4==0:
    if year%100!=0:
        print("Leap year")
    else:
        if year%400==0:
            print("Leap year")
        else:
            print("Not leap year")
else:
    print("Not leap year")
