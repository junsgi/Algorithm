# https://www.acmicpc.net/problem/9466
import sys
sys.setrecursionlimit(100_000)

swi = False
checkNode = -1
def DFS(node):
  global swi, checkNode

  # 현재 노드가 어느 그룹에 속해있다면 return
  if node in noGroup or node in group:
    swi = False
    return
  
  # 방문 했던 노드에 도착하면
  # 현재 노드를 기억하고 다시 만날 때까지 모든 노드를 group 집합에 삽입
  if visit[node]:
    checkNode = node
    swi = True
    return
  
  visit[node] = 1
  DFS(arr[node])

  # 멤버 삽입
  if swi:
    group.add(node)
  else:
    noGroup.add(node)

  # 만약 다시 만났다면 이전 노드부턴 모두 그룹에 속하지 못한 유저
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