# https://www.acmicpc.net/problem/3967
dire = [[1, -1], [0, 2], [-1, -1]]
idxs = []
visit = [0] * 14
graph = [list(input()) for _ in range(5)]
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == 'x':
            idxs.append([i, j])
        elif graph[i][j] != '.':
            visit[ord(graph[i][j]) - 65] = 1


def PRINT():
    for g in graph:
        print(''.join(g))

def CHECK():
    t1 = [0, 4, 0]
    t2 = [4, 4, 0]
    for i in range(10):
        t1[2] += int(graph[t1[0]][t1[1]], 36) - 9
        t2[2] += int(graph[t2[0]][t2[1]], 36) - 9

        if i > 0 and i % 3 == 0:
            if not (t1[2] == 26 and t2[2] == 26):
                return False
            else:
                t1[2] = int(graph[t1[0]][t1[1]], 36) - 9
                t2[2] = int(graph[t2[0]][t2[1]], 36) - 9

        if i < 9:
            t1[0] += dire[i // 3][0]
            t1[1] += dire[i // 3][1]

            t2[0] += dire[(len(dire) - 1) - i // 3][0]
            t2[1] += dire[(len(dire) - 1) - i // 3][1]
    return True

def rec(depth):
    if depth == len(idxs):
        swi = CHECK()
        if swi:
            PRINT()
            exit()
        return
    
    for i in range(12):
        if visit[i]: continue
        visit[i] = 1
        graph[idxs[depth][0]][idxs[depth][1]] = chr(i + 65)
        rec(depth + 1)
        visit[i] = 0
rec(0)