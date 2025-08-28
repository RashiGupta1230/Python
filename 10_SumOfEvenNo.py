def sum_of_evens(A):
    total = 0
    i = 2
    while i <= A:
        total += i
        i += 2
    return total
A = 10
print(sum_of_evens(A))