# https://www.acmicpc.net/problem/9466
def DFS(node, st):
  return DFS(arr[node], st)

n = int(input())
answer = 0
swi = False
for _ in range(n):
  N = int(input())
  arr = list(map(int, input().split()))

  for stu in arr:
    t = DFS(stu, stu)