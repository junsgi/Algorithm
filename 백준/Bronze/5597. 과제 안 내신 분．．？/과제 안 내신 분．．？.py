result=[None] * 28
a = {i for i in range(1,31)}
for j in range(28):
    num = int(input())
    result[j] = num
for k in sorted(list(a - set(result))):
    print(k)