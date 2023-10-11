# https://www.acmicpc.net/problem/14499
N, M, dx, dy, com = map(int, input().split())
grp = [list(map(int, input().split())) for _ in range(N)]
com = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0, 0] # 윗 

mv = [0, 
      [0, 4, 2, 1, 6, 5, 3], # 동
      [0, 3, 2, 6, 1, 5, 4], # 서
      [0, 5, 1, 3, 4, 6, 2], # 북
      [0, 2, 6, 3, 4, 1, 6], # 남
      ]