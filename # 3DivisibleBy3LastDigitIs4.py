# 3. WAP to check if the number is divisible by 3 and the last digit is 4.
n=int(input("Enter number: "))
last_digit=n%10
if n%3==0 and last_digit==4:
    print("Yes")
else:
    print("No")