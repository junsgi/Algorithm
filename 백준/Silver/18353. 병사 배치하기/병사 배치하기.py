n = int(input())
arr = tuple(map(int, input().split()))[::-1]
DP = [arr[0]]
answer =  0
for i in range(1, n):
    if arr[i] > DP[-1]:
        DP.append(arr[i])
    else:
        answer += 1
        left = 0
        right = len(DP) - 1
        while left <= right:
            mid = (left + right) // 2
            if DP[mid] == arr[i]:
                break
            elif DP[mid] < arr[i]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            DP[left] = arr[i]
print(answer)