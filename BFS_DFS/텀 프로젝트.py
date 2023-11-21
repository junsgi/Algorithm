# https://www.acmicpc.net/problem/9466
Rota = set()
Team = set()
visit = set()

def DFS(node, st):
  global Rota, Team, visit
  visit.add(node)  
  return DFS(arr[node], st)

n = int(input())
answer = 0
for _ in range(n):
  N = int(input())
  arr = list(map(int, input().split()))

  for stu in arr:
    t = DFS(stu, stu)