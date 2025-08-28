N = int(input())
sum_digits = 0
n = abs(N)
while n > 0:
    sum_digits += n % 10
    n //= 10
print(sum_digits)