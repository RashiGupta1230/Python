# 4. WAP to check if the number is divisible by 7 or if the last digit is 5.
n=int(input("Enter number: "))
last_digit=n%10
if n%7==0 or last_digit==5:
    print("Yes")
else:
    print("No")