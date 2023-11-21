# https://www.acmicpc.net/problem/9466
Rota = set()
Team = set()
visit = set()

def DFS(node, st):
  global Rota, Team, visit

  if node in visit:
    result = 0
    if node in Rota or node != st:
      Rota |= visit
      result = 1
    elif node in Team or node == st:
      Team |= visit
      result = 2
    return result

  visit.add(node)  
  return DFS(arr[node], st)

n = int(input())
answer = 0
for _ in range(n):
  N = int(input())
  arr = list(map(int, input().split()))

  for stu in arr:
    t = DFS(stu, stu)