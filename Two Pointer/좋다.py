# https://www.acmicpc.net/problem/1253
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 0
for i in range(n):
    left = 0
    right = n - 1
    sum = 0
    while left != right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue
        sum = arr[left] + arr[right]
        if arr[i] < sum:
            right -= 1
        elif arr[i] > sum:
            left += 1
        else:
            ans += 1
            break
print(ans)