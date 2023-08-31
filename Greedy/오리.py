import sys
input = sys.stdin.readline
duck = input().strip()
check = {'q' : 0, 'u' : 1, 'a' : 2, 'c' : 3, 'k' : 4}
a = [0, 0, 0, 0]
ans = 0
for i in duck:
    if i == 'q':
        a[0] += 1
    elif a[check[i] - 1] > 0:
        a[check[i] - 1] -= 1
        if i != 'k': # index 
            a[check[i]] += 1

    # 이 전 글자가 존재하지 않으면 녹음 소리가 올바르지 않음
    else:
        print(-1)
        exit()
    ans = max(ans, sum(a))
if any(a):
    print(-1)
else:
    print(ans)
