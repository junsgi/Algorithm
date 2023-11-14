a = input()
for i in range(len(a) // 2):
    if a[i] != a[len(a) - 1 - i]:
        print(0)
        exit()
print(1)