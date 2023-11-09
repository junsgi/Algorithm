# https://school.programmers.co.kr/learn/courses/30/lessons/43162
def dfs(x, g):
    for i in range(len(g[x])):
        if g[x][i] == 1:
            g[x][i] = 0
            dfs(i, g)
def solution(n, computers):
    answer = 0
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if computers[i][j] == 1:
                answer += 1
                computers[i][j] = 0
                dfs(i, computers)
    return answer