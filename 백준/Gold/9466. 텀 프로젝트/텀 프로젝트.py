# https://www.acmicpc.net/problem/9466
import sys
sys.setrecursionlimit(100_000)

swi = False
checkNode = -1
def DFS(node):
  global swi, checkNode
  if node in noGroup or node in group:
    swi = False
    return
  
  if visit[node]:
    checkNode = node
    swi = True
    return
  
  visit[node] = 1
  DFS(arr[node])

  if swi:
    group.add(node)
  else:
    noGroup.add(node)

  if node == checkNode:
    swi = False
  return

n = int(input())
group = set()
noGroup = set()
for _ in range(n):
  N = int(input())
  arr = [-1]
  arr.extend(list(map(int, input().split())))
  visit = [0] * (N + 1)
  group.clear()
  noGroup.clear()

  for stu in range(1, N + 1):
    if not (stu in group or stu in noGroup):
      DFS(stu)
  print(len(noGroup))