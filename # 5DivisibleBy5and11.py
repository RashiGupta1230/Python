# 5. Take an integer A as input. You have to tell whether A is divisible by both 5 and 11 or not.
a=int(input("Enter number: "))
if a%5==0 and a%11==0:
    print("Yes")
else:
    print("No")