def sosu_find(num):
    x = []
    a = num
    while num:
        result = a % num
        if result == 0:
            x.append(result)
        num-=1
    if len(x) == 2:
        return "sosu"
    else:
        return 1

M = int(input())
N = int(input())
result=[]
for i in range(M,N+1):
    if sosu_find(i) != "sosu": continue
    else:
        result.append(i)
if sum(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))