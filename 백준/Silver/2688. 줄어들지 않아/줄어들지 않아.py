DP = [[0] * 10 for _ in range(65)]
for i in range(10): DP[1][i] = 1
for i in range(2, 65):
    for j in range(10):
        DP[i][j] = sum(DP[i - 1][j:])
answer = []
for i in DP:
    answer.append(sum(i))

n = int(input())
for _ in range(n):
    print(answer[int(input())])