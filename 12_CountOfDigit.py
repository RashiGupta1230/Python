N = int(input())
count = 0
num = abs(N)  
if num == 0:
    count = 1
else:
    while num > 0:
        num //= 10
        count += 1
print(count)