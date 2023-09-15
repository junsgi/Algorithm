# https://www.acmicpc.net/problem/17135
import sys
input = sys.stdin.readline
n, m, d = map(int, input().split())
enemy = []
casle = []
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
    for j in range(m):
        if a[i][j] == 1:
            enemy.append((i, j))

"""
1. 궁수는 3명 배치한다.
2. 궁수가 공격하는 적은 
 - 거리가 D이하인 적 중에서 가장 가까운 적
 - 여럿일 경우 가장 왼쪽에 있는 적
 - (distance, y)
3. 같은 적이 여러 궁수에게 공격당할 수 있다.
4. 공격 받으면 제외
5. 적은 아래로 한 칸 이동하며 n + 1에 도착하면 제외된다.
6. 모든 적이 사라지면 게임 종료
"""