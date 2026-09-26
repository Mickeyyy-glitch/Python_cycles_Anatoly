x_start = -4
x_end = 10
dx = 1
x = x_start

print(f"{'x':>8} | {'y':>10}")
print("-" * 23)

while x <= x_end + 1e-9:
    if -4 <= x <= -2:
        y = x + 3
    elif -2 < x <= 4:
        y = -0.5 * x
    elif 4 < x <= 6:
        y = -2
    elif 6 < x <= 10:
        y = -2 + (4 - (x - 8) ** 2) ** 0.5

    print(f"{x:8.2f} | {y:10.4f}")

    x += dx