f = [1] * 117
for i in range(4, 117): f[i] = f[i - 1] + f[i - 3]
print(f[int(input())])