def is_odd(n):
    return n % 2 == 1


L = filter(is_odd, [1, 2, 4, 7, 8, 9, 10])
print(list(L))
