# 3_SumOfDigits
num=int(input("Enter a number:"))
count=0
while num>0:
    digit = num%10
    count+=digit
    num=num//10
print("Sum of digit:", count)