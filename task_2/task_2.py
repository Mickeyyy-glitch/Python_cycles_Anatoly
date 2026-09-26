for x in range(10, 100):
    if ((x // 10) ** 2 + (x % 10) ** 2) % 17 == 0:
        print(x)