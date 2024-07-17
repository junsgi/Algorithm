n=int(input())
arr=list(map(int,input().split()))
DP = [[0]*21 for _ in range(n)]
DP[0][arr[0]]=1
for i in range(1, n-1):
  for j in range(21):
    if DP[i-1][j]!=0:
      if j - arr[i] >= 0: DP[i][j-arr[i]] += DP[i-1][j]
      if j + arr[i] <= 20: DP[i][j+arr[i]] += DP[i-1][j]
print(DP[n-2][arr[-1]])