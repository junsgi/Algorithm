arr = [(i + 1) * i // 2 for i in range(1, 700) if (i + 1) * i // 2 <= 300_000]
nums = []
temp = 0
DP = [999999] * 300_001
for i in arr:
    if i + temp <= 300_000:
        DP[i + temp] = 1
        temp = i + temp
        nums.append(temp)
    else:
        break
for i in range(1, 300_001):
    for j in nums:
        if i < j: break
        DP[i] = min(DP[i], DP[i - j] + 1)
print(DP[int(input())])
