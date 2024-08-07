n = int(input())
arr = [float(input())]
for _ in range(n - 1):
    f = float(input())
    arr.append(max(arr[-1] * f, f))
print("%.3f" % (max(arr)))