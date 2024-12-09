def solution(rows, columns, queries):
    answer = []
    arr = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]
    for x1, y1, x2, y2 in queries:
        x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        arr[x1][y1], temp = arr[x1 + 1][y1], arr[x1][y1]
        res = temp
        for i in range(y1 + 1, y2 + 1):
            arr[x1][i], temp = temp, arr[x1][i]
            res = min(res, temp)
            
        for i in range(x1 + 1, x2 + 1):
            arr[i][y2], temp = temp, arr[i][y2]
            res = min(res, temp)
        for i in range(y2 - 1, y1 - 1, -1):
            arr[x2][i], temp = temp, arr[x2][i]
            res = min(res, temp)
        for i in range(x2 - 1, x1, -1):
            arr[i][y1], temp = temp, arr[i][y1]
            res = min(res, temp)
        answer.append(res)
    return answer