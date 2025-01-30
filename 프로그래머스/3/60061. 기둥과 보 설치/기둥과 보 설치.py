def solution(n, build_frame):
    answer = []
    arr = [[[0 for _ in range(n + 2)] for __ in range(n + 2)] for ___ in range(2)]
    def pillar(x, y):
        case1 = y == 0 # 지면이거나
        case2 = arr[0][x][y - 1] # 아래에 기둥이 있거나
        case3 = arr[1][x][y] # 보가 있거나 (시작점)
        case4 = (x - 1 >= 0 and arr[1][x - 1][y]) # 보가 있거나 (끝점)
        return case1 or case2 or case3 or case4
    def beam(x, y):
        case1 = arr[0][x][y - 1] # 아래에 기둥이 있거나 (시작점)
        case2 = arr[0][x + 1][y - 1] # 아래에 기둥이 있거나 (끝점)
        case3 = x > 0 and arr[1][x - 1][y] + arr[1][x + 1][y] >= 2 # 보 양쪽에 또 다른 보가 있다면
        return case1 or case2 or case3
    def delete(x, y, a):
        arr[a][x][y] -= 1 # 일단 삭제
        res = True
        for i in range(n + 1):
            for j in range(n + 1):
                if arr[0][i][j] and not pillar(i, j):
                    res = False
                if arr[1][i][j] and not beam(i, j):
                    res = False
                if not res: break
            if not res:
                break
        arr[a][x][y] += 1
        return res
    for x, y, a, b in build_frame:
        if a:
            if b and y > 0 and beam(x, y): # 보를 설치 (양쪽에 보가 있던가 아래쪽에 기둥이 있다면 설치)
                arr[a][x][y] += 1
            elif b == 0 and delete(x, y, a): # 보를 삭제
                arr[a][x][y] -= 1
        else:
            if b and pillar(x, y): # 기둥 설치
                arr[a][x][y] += 1
            elif b == 0 and delete(x, y, a): # 기둥 삭제
                arr[a][x][y] -= 1
        # print(x, y, a, b)
        # for i in arr[0][:n + 1]:
        #     print(i[:n + 1])
        # print()     
        # for i in arr[1][:n + 1]:
        #     print(i[:n + 1])
        # print("---")
            
    for i in range(n + 1):
        for j in range(n + 1):
            if arr[0][i][j]:
                answer.append([i, j, 0])
            if arr[1][i][j]:
                answer.append([i, j, 1])
                
    return answer