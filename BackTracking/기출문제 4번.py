# 1 -> 3
# 2 -> 4
# 5 벽, 0 빈칸

dire = [[-1, 0], [1, 0], [0, -1], [0, 1]]
answer = 2 ** 31

def BACK(graph, rx, ry, bx, by, visit, depth, S, B):
    global answer
    # 옮기고 보니 부딪혔다면
    if rx == bx and ry == by : return

    # 백트래킹
    if answer <= depth:
        return
    
    # 도착하면 
    if S and B:
        answer = depth
        return
    
    for i in range(4):
        Rx, Ry = 0, 0
        
        if S: # 도착했다면 그대로
            Rx, Ry = rx, ry
        else: # 도착못했으면 옮김
            Rx, Ry = dire[i][0] + rx, dire[i][1] + ry
            
        if not (0 <= Rx < len(graph) and 0 <= Ry < len(graph[0])) :
            continue
            
        # 부딪힌다면
        if Rx == bx and Ry == by: continue
        
        if (not S and visit[0][Rx][Ry]) or graph[Rx][Ry] == 5 : continue
        
        visit[0][Rx][Ry] = 1
        
        for j in range(4):
            Bx, By = 0, 0
            if B:
                Bx, By = bx, by
            else:
                Bx, By = dire[j][0] + bx, dire[j][1] + by
            
            if not (0 <= Bx < len(graph) and 0 <= By < len(graph[0])) :
                continue
            if Bx == Rx and By == Ry: continue
            if (not B and visit[1][Bx][By]) or graph[Bx][By] == 5: continue
            
            visit[1][Bx][By] = 1
            BACK(graph, Rx, Ry, Bx, By, visit, depth + 1, graph[Rx][Ry] == 3, graph[Bx][By] == 4)
            visit[1][Bx][By] = 0
        visit[0][Rx][Ry] = 0
        
        # 파란거 먼저@####################################
        Bx, By = 0, 0
        if S: # 도착했다면 그대로
            Rx, Ry = rx, ry
        else: # 도착못했으면 옮김
            Rx, Ry = dire[i][0] + rx, dire[i][1] + ry
            
        if not (0 <= Rx < len(graph) and 0 <= Ry < len(graph[0])) :
            continue
            
        # 부딪힌다면
        if Rx == bx and Ry == by: continue
        
        if (not S and visit[0][Rx][Ry]) or graph[Rx][Ry] == 5 : continue
        
        visit[0][Rx][Ry] = 1
        
        for j in range(4):
            Bx, By = 0, 0
            if B:
                Bx, By = bx, by
            else:
                Bx, By = dire[j][0] + bx, dire[j][1] + by
            
            if not (0 <= Bx < len(graph) and 0 <= By < len(graph[0])) :
                continue
            if Bx == Rx and By == Ry: continue
            if (not B and visit[1][Bx][By]) or graph[Bx][By] == 5: continue
            
            visit[1][Bx][By] = 1
            BACK(graph, Rx, Ry, Bx, By, visit, depth + 1, graph[Rx][Ry] == 3, graph[Bx][By] == 4)
            visit[1][Bx][By] = 0
            
        
def solution(maze):
    global answer
    rx, ry, bx, by = 0, 0, 0, 0
    
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                rx, ry = i, j
            if maze[i][j] == 2:
                bx, by = i, j
                
    visit = [[[0] * len(maze[0]) for _ in range(len(maze))] for _ in range(2)]
    visit[0][rx][ry] = visit[1][bx][by] = 1
    BACK(maze, rx, ry, bx, by, visit, 0, False, False)

    if answer == 2 ** 31:
        answer = 0
    return answer