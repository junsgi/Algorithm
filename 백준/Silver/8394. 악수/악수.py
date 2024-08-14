x = 0
y = 1
z = 1
for _ in range(int(input())):
    x, y, z = y % 10, (x + y) % 10, (x + y) % 10
print(z)
