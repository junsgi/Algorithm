# https://www.acmicpc.net/problem/2467
import sys
input = sys.stdin.readline

n = int(input())
MAX = 0x7fffffff
arr = sorted(list(map(int, input().split())))
answer = [MAX, MAX]
for i in range(n):
    target = -arr[i]
    le = i + 1
    ri = n - 1
    temp = [arr[i], MAX]
    while le <= ri:
        mid = (le + ri) // 2

        if target < arr[mid] :
            ri = mid - 1
        elif target > arr[mid]:
            le = mid + 1
        else:
            answer[0] = target
            answer[1] = arr[mid]
            break
    if le < n:
        temp[1] = arr[le]
        t1 = abs(sum(temp))
        t2 = abs(sum(answer))
        if t1 < t2:
            answer[0] = temp[0]
            answer[1] = temp[1]
    
    if i < ri:
        temp[1] = arr[ri]
        t1 = abs(sum(temp))
        t2 = abs(sum(answer))
        if t1 < 0 : t1 = -t1
        if t2 < 0 : t2 = -t2
        if t1 < t2:
            answer[0] = temp[0]
            answer[1] = temp[1]
print(*answer)