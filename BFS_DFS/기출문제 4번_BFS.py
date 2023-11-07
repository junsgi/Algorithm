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
BACKTRACKING
# https://school.programmers.co.kr/learn/courses/19344/lessons/242261

dire = [[-1, 0], [1, 0], [0, -1], [0, 1]]
answer = 2 ** 31

def CHECK(a, b, g):
    return 0 <= a < len(g) and 0 <= b < len(g[0])

def BACK(graph, visit, RB, R, B, depth):
    global answer
    if answer <= depth :return
    if R and B:
        answer = depth
        return
    
    rx, ry, bx, by = RB
    Rx, Ry, Bx, By = 0, 0, 0, 0
    
    # 빨간거 부터 옮기는 코드
    for i in range(4):
        Rx, Ry = rx + dire[i][0], ry + dire[i][1]
        if R:
            Rx, Ry = rx, ry
        if not CHECK(Rx, Ry, graph) : continue
        if not R and visit[0][Rx][Ry] : continue
        if Rx == bx and Ry == by: continue
        if graph[Rx][Ry] == 5 : continue
        visit[0][Rx][Ry] = 1
        for j in range(4):
            Bx, By = bx + dire[j][0], by + dire[j][1]
            if B:
                Bx, By = bx, by
            if not CHECK(Bx, By, graph) : continue
            if not B and visit[1][Bx][By] : continue
            if Bx == Rx and By == Ry: continue
            if graph[Bx][By] == 5 : continue
            visit[1][Bx][By] = 1
            BACK(graph, visit, [Rx, Ry, Bx, By], graph[Rx][Ry] == 3, graph[Bx][By] == 4, depth + 1)
            visit[1][Bx][By] = 0
        visit[0][Rx][Ry] = 0

    # 파란거부터 옮기는 코드
    for i in range(4):
        Bx, By = bx + dire[i][0], by + dire[i][1]
        if B:
            Bx, By = bx, by
        if not CHECK(Bx, By, graph) : continue
        if not B and visit[1][Bx][By] : continue
        if Bx == rx and By == ry: continue
        if graph[Bx][By] == 5 : continue
        visit[1][Bx][By] = 1

        for j in range(4):
            Rx, Ry = rx + dire[j][0], ry + dire[j][1]
            if R:
                Rx, Ry = rx, ry
            if not CHECK(Rx, Ry, graph) : continue
            if not R and visit[0][Rx][Ry] : continue
            if Rx == Bx and Ry == By: continue
            if graph[Rx][Ry] == 5 : continue
            visit[0][Rx][Ry] = 1
            BACK(graph, visit, [Rx, Ry, Bx, By], graph[Rx][Ry] == 3, graph[Bx][By] == 4, depth + 1)
            visit[0][Rx][Ry] = 0
        visit[1][Bx][By] = 0

def solution(maze):
    global answer
    RB = [0, 0, 0, 0]
    
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                RB[0], RB[1] = i, j
            if maze[i][j] == 2:
                RB[2], RB[3] = i, j
                
    visit = [[[0] * len(maze[0]) for _ in range(len(maze))] for _ in range(2)]
    visit[0][RB[0]][RB[1]] = visit[1][RB[2]][RB[3]] = 1
    BACK(maze, visit, RB, False, False, 0)

    if answer == 2 ** 31:
        answer = 0
    return answer


"""