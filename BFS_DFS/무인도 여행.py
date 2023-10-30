import sys 
sys.setrecursionlimit(100**2)
sum1 = 0
def DFS(x, y, maps):
    global sum1
    if not (0 <= x < len(maps) and 0 <= y < len(maps[0])): 
        return
    if maps[x][y] == 'X':
        return
    
    sum1 += int(maps[x][y])
    maps[x][y] = 'X'
    
    DFS(x + 1, y, maps)
    DFS(x - 1, y, maps)
    DFS(x, y + 1, maps)
    DFS(x, y - 1, maps)
    
def solution(maps):
    global sum1
    answer = []
    for i in range(len(maps)):
        maps[i] = list(maps[i])
        
    
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] != 'X':
                sum1 = 0
                DFS(i, j, maps)
                answer.append(sum1)
    return sorted(answer) if len(answer) > 0 else [-1]