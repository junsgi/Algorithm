# https://school.programmers.co.kr/learn/courses/19344/lessons/242261
from collections import deque
dire = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def CHECK(a, b, g):
    return not (0 <= a < len(g) and 0 <= b < len(g[0])) 

def BFS(graph, visit, RB):
    global answer
    que = deque()
    RB.extend([0, False, False])
    que.append(RB)
    visit[RB[0]][RB[1]][RB[2]][RB[3]] = 1
    visit[RB[2]][RB[3]][RB[0]][RB[1]] = 1
    
    while que:
        rx, ry, bx, by, depth, R, B = que.popleft()
        
        if R and B:
            return depth
        # 빨간거 부터 옮기는 코드
        for i in range(4):
            Rx, Ry = rx + dire[i][0], ry + dire[i][1]
            if R:
                Rx, Ry = rx, ry
            if CHECK(Rx, Ry, graph) : continue
            if Rx == bx and Ry == by: continue
            if graph[Rx][Ry] == 5 : continue
            
            for j in range(4):
                Bx, By = bx + dire[j][0], by + dire[j][1]
                if B:
                    Bx, By = bx, by
                if CHECK(Bx, By, graph) : continue
                if visit[Rx][Ry][Bx][By]: continue
                if Bx == Rx and By == Ry: continue
                if graph[Bx][By] == 5 : continue
                visit[Rx][Ry][Bx][By] = 1
                que.append([Rx, Ry, Bx, By, depth + 1, graph[Rx][Ry] == 3, graph[Bx][By] == 4])
                

        # 파란거부터 옮기는 코드
        for i in range(4):
            Bx, By = bx + dire[i][0], by + dire[i][1]
            if B:
                Bx, By = bx, by
            if CHECK(Bx, By, graph) : continue
            if Bx == rx and By == ry: continue
            if graph[Bx][By] == 5 : continue
            
            
            for j in range(4):
                Rx, Ry = rx + dire[j][0], ry + dire[j][1]
                if R:
                    Rx, Ry = rx, ry
                if CHECK(Rx, Ry, graph) : continue
                if visit[Rx][Ry][Bx][By]: continue
                if Rx == Bx and Ry == By: continue
                if graph[Rx][Ry] == 5 : continue
                visit[Rx][Ry][Bx][By] = 1
                que.append([Rx, Ry, Bx, By, depth + 1, graph[Rx][Ry] == 3, graph[Bx][By] == 4])
    return 0


def solution(maze):
    global answer
    RB = [None] * 4
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                RB[0], RB[1] = i, j
            if maze[i][j] == 2:
                RB[2], RB[3] = i, j
                
    visit2 = [[[[0] * 4 for _ in range(4)] for __ in range(4)] for __ in range(4)]
    return BFS(maze, visit2, RB)






"""
[
[5, 0, 0, 5],
[1, 2, 4, 3],
[5, 5, 5, 5],
[5, 5, 5, 5],
]


[
[5, 5, 5, 5],
[1, 2, 0, 5],
[5, 4, 0, 5],
[5, 3, 5, 5],
]

[
[5, 5, 5, 5],
[1, 3, 0, 5],
[5, 4, 0, 5],
[5, 3, 5, 5],
]

[
[5, 5, 5, 5],
[1, 3, 0, 5],
[5, 0, 2, 5],
[5, 5, 5, 5],
]

[
[5, 1, 0, 0],
[5, 0, 0, 0],
[0, 0, 3, 4],
[2, 5, 5, 5]
]

[
[1, 5, 5, 2],
[0, 5, 5, 0],
[0, 0, 0, 0],
[4, 0, 0, 3]
]

[
[1, 0, 0, 2],
[4, 0, 0, 3],
[0, 0, 0, 0],
[0, 0, 0, 0]
]

[
[3, 4, 5, 2],
[1, 5, 5, 0],
[0, 0, 0, 0],
[0, 0, 0, 0]
]
"""