A = int(input("Enter A: "))
B = int(input("Enter B: "))
result = 1
counter = 0
while counter < B:
    result *= A
    counter += 1
print(str(A) + "^" + str(B) + " = " + str(result))