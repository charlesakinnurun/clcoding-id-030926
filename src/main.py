x = map(lambda n: n // 2,
        filter(lambda n: n % 2, range(8)))
print(sum(x))