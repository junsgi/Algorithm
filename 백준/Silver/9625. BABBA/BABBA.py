n = int(input())
x1, x2, y1, y2, a1, a2 = 0, 1, 1, 0, 0, 1
for _ in range(1, n):
    a1, a2 = x1 + y1, x2 + y2
    x1, x2, y1, y2 = a1, a2, x1, x2
print(a1, a2)