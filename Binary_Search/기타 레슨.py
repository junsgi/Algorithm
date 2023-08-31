import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
a.sort()

# 블루레이가 mid보다 작거나 같다면
le = 1
ri = 1_000_000_000
mid = 0
ans = 0
while le <= ri:
    mid = (le + ri) // 2
    cnt = 0
    sum = 0
    check = False
    for num in a:
        sum += num
        if mid <= sum:
            cnt += 1
            sum = num
        
        if cnt > m:
            break
    
    if cnt == m:
        ans = min(ans, mid)
    if cnt > m:
        le = mid + 1
    else:
        ri = mid - 1

print(ri, mid, le, ans)