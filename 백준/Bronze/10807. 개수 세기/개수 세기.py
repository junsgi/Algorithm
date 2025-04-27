n = int(input())
a = list(map(int, input().split()))
v = int(input())
count = 0
for i in range(len(a)//2):
    if v == a[i]: count += 1
    if v == a[len(a)-i-1]: count += 1
if n % 2 == 0:
    print(count)
else:
    if a[n // 2] == v:
        print(count+1)
    else:
        print(count)