# 7. Read three angles of a triangle and determine their type (Right, Obtuse, Acute).
a=int(input("Enter first angle: "))
b=int(input("Enter second angle: "))
c=int(input("Enter third angle: "))
if a==90 or b==90 or c==90:
    print("Right triangle")
elif a>90 or b>90 or c>90:
    print("Obtuse triangle")
else:
    print("Acute triangle")