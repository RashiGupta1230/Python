# 12. You are given 3 integer angles of a triangle. Check if the triangle is valid or not.
a=int(input("Enter first angle: "))
b=int(input("Enter second angle: "))
c=int(input("Enter third angle: "))
if a+b+c==180:
    print("Valid triangle")
else:
    print("Invalid triangle")
