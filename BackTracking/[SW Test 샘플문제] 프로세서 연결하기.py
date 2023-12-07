# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4suNtaXFEDFAUf
"""
단순한 구현 문제
사용된 코어와 사용할 코어의 개수가 최대로 사용했던 코어의 개수보다 적으면 더이상 탐색하지 않는다.
"""
dire = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def DRAW(x, y, d, graph):
    tx, ty = x + dire[d][0], y + dire[d][1]
    while 0 <= tx < len(graph) and 0 <= ty < len(graph):
        if graph[tx][ty] == 1 or visit[tx][ty] == 1:
            return [0, 0]
        tx += dire[d][0]
        ty += dire[d][1]
    
    result = 0
    tx, ty = x + dire[d][0], y + dire[d][1]
    while 0 <= tx < len(graph) and 0 <= ty < len(graph):
        visit[tx][ty] = 1
        result += 1
        tx += dire[d][0]
        ty += dire[d][1]

    return [1, result]


def REMOVE(x, y, d, graph):
    tx, ty = x + dire[d][0], y + dire[d][1]
    while 0 <= tx < len(graph) and 0 <= ty < len(graph):
        visit[tx][ty] = 0
        tx += dire[d][0]
        ty += dire[d][1]

def BACK(depth: int, useCore : int, value : int):
    global ans, MaxCore
    # 남은 코어를 전부 사용해도 최대로 코어를 사용했을 때보다 적으면 return
    if MaxCore > useCore + (len(location) - depth): return

    if depth == len(location):
        # 사용한 코어의 개수가 같을 때 최솟값 구하기
        if useCore == MaxCore and value > ans : return
        MaxCore = useCore
        ans = value
        return
    
    for i in range(4):

        us = DRAW(location[depth][0], location[depth][1], i, graph)
        useCore += us[0]
        value += us[1]
        BACK(depth + 1, useCore, value)
        if us[0] == 1: REMOVE(location[depth][0], location[depth][1], i, graph)
        useCore -= us[0]
        value -= us[1]

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    location = []
    graph = []
    visit = [[0] * N for _ in range(N)]
    for i in range(N):
        arr = list(map(int, input().split()))
        for j in range(N):
            if 0 < i < N - 1 and 0 < j < N - 1 and arr[j]:
                location.append([i, j])
        graph.append(arr)
    ans = 0x7fffffff
    MaxCore = 0
    BACK(0, 0, 0)
    print(f"#{test_case} {ans}")
