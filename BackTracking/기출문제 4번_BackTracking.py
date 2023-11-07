# https://school.programmers.co.kr/learn/courses/19344/lessons/242261
dire = [[-1, 0], [1, 0], [0, -1], [0, 1]]
answer = 2 ** 31

def CHECK(a, b, g):
    return 0 <= a < len(g) and 0 <= b < len(g[0])
start = [0, 0, 0, 0]
def BACK(graph, visit, RB, R, B, depth):
    global answer
    if answer <= depth :return
    if R and B:
        answer = depth
        return
    rx, ry, bx, by = RB
    print(RB)
    Rx, Ry, Bx, By = 0, 0, 0, 0
    
    # 빨간거 부터 옮기는 코드
    if not R:
        for i in range(4):
            Rx, Ry = rx + dire[i][0], ry + dire[i][1]
            if R:
                Rx, Ry = rx, ry
            if not CHECK(Rx, Ry, graph) : continue
            if Rx == bx and Ry == by: continue
            if Rx == start[0] and Ry == start[1]: continue
            if graph[Rx][Ry] == 5 : continue

            for j in range(4):
                Bx, By = bx + dire[j][0], by + dire[j][1]
                if B:
                    Bx, By = bx, by
                if not CHECK(Bx, By, graph) : continue
                if visit[Rx][Ry][Bx][By] : continue
                if Bx == Rx and By == Ry: continue
                if Bx == start[2] and By == start[3] : continue
                if graph[Bx][By] == 5 : continue
                visit[Rx][Ry][Bx][By] = 1
                BACK(graph, visit, [Rx, Ry, Bx, By], graph[Rx][Ry] == 3, graph[Bx][By] == 4, depth + 1)
                #visit[Rx][Ry][Bx][By] = 0
    if not B:
        # 파란거부터 옮기는 코드
        for i in range(4):
            Bx, By = bx + dire[i][0], by + dire[i][1]
            if B:
                Bx, By = bx, by
            if not CHECK(Bx, By, graph) : continue
            if Bx == rx and By == ry: continue
            if Bx == start[2] and By == start[3] : continue

            if graph[Bx][By] == 5 : continue

            for j in range(4):
                Rx, Ry = rx + dire[j][0], ry + dire[j][1]
                if R:
                    Rx, Ry = rx, ry
                if not CHECK(Rx, Ry, graph) : continue
                if visit[Rx][Ry][Bx][By] : continue
                if Rx == Bx and Ry == By: continue
                if Rx == start[0] and Ry == start[1]: continue

                if graph[Rx][Ry] == 5 : continue
                visit[Rx][Ry][Bx][By]  = 1
                BACK(graph, visit, [Rx, Ry, Bx, By], graph[Rx][Ry] == 3, graph[Bx][By] == 4, depth + 1)
                #visit[Rx][Ry][Bx][By] = 0

def solution(maze):
    global answer
    RB = [0, 0, 0, 0]
    
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                RB[0], RB[1] = i, j
            if maze[i][j] == 2:
                RB[2], RB[3] = i, j
                
    visit = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for __ in range(4)]
    visit[RB[0]][RB[1]][RB[2]][RB[3]] = 1
    start[0] = RB[0]
    start[1] = RB[1]
    start[2] = RB[2]
    start[3] = RB[3]

    BACK(maze, visit, RB, False, False, 0)

    if answer == 2 ** 31:
        answer = 0
    return answer
print(solution(	[[3, 4, 5, 2], [1, 5, 5, 0], [0, 0, 0, 0], [0, 0, 0, 0]]))