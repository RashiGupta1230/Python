A = int(input())
i = 1
total = 0
while i <= A:
    if i % 2 == 1:
        total += i
    i += 1
print(total)