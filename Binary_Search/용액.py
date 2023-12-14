# https://www.acmicpc.net/problem/2467
import sys
input = sys.stdin.readline
n = int(input())
MAX = 0x7fffffff
arr = list(map(int, input().split()))
answer = [MAX, MAX]
for i in range(n):
    target = -arr[i]
    le = i + 1
    ri = n - 1
    while le <= ri:
        mid = (le + ri) // 2

        if target < arr[mid] :
            ri = mid - 1
        elif target > arr[mid]:
            le = mid + 1
        else:
            print(arr[i], arr[mid])
            exit()
    

    if le < n and abs(sum(answer)) > abs(arr[i] + arr[le]):
        answer[0], answer[1] = arr[i], arr[le]
    
    if i < ri and abs(sum(answer)) > abs(arr[i] + arr[ri]):
        answer[0], answer[1] = arr[i], arr[ri]
print(*answer)