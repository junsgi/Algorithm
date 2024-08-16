n = int(input())
x, y, z = 1, 1, 2
if n < 2:
    print(1)
else:
    for _ in range(n - 1):
        x, y, z = y % 1_000_000_007, (x + y + 1) % 1_000_000_007, (x + y + 1) % 1_000_000_007
    print(z % 1_000_000_007)