# 15. Accept the percentage from the user and display the grade.
p=int(input("Enter percentage: "))
if p>=90:
    print("A")
elif p>=80:
    print("B")
elif p>=70:
    print("C")
elif p>=60:
    print("D")
else:
    print("F")