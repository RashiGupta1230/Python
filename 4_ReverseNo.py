a=int(input("Enter a no.:"))
count=0
while a>0:
    digit=a%10
    count=count*10+digit
    a=a//10
print("Reverse no.:",count)
