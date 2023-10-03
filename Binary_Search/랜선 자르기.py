# https://www.acmicpc.net/problem/1654
K, N = map(int, input().split())
lan = []
for _ in range(K):
    lan.append(int(input()))
le = 1
ri = 0x7fffffff
mid = 0
ans = 0
while le <= ri:
    mid = (le + ri) // 2
    cnt = 0
    for cm in lan:
        cnt += cm // mid
        if cnt > N:
            break
    if cnt < N :
        ri = mid - 1
    else:
        ans = max(ans, mid)
        le = mid + 1
print(ans)