# https://school.programmers.co.kr/learn/courses/30/lessons/68936
def solution(arr):
    answer = [0, 0] 
    check = [[0] * len(arr) for _ in range(len(arr))]
    def div(x, y, length, size):
        # 방문했다면 돌아감
        if check[x][y]:  return
        # 현재 크기가 1이면 갱신과 방문체크 후 돌아감 
        if size == 1:
            answer[arr[x][y]] += 1
            check[x][y] = 1
            return
        
        one = 0 # 0의 개수
        zero = 0 # 1의 개수
        for i in range(x, x + length):
            for j in range(y, y + length):
                if one and zero: # 0과 1이 섞여있다면 멈춥니다.
                    break
                    
                if arr[i][j]: one += 1
                else : zero += 1
                
            if one and zero:
                break
        
        if (not one and zero) or (one and not zero):
            answer[arr[x][y]] += 1
            for i in range(x, x + length):
                for j in range(y, y + length):
                    check[i][j] = 1
        l = length // 2
        s = size // 4
        # 분할정복
        div(x, y, l, s)
        div(x, y + l, l, s)
        div(x + l, y, l, s)
        div(x + l, y + l , l, s)
    div(0, 0, len(arr), len(arr) ** 2)
    return answer