def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key = lambda x : (x[col - 1], -x[0]))
    data = [None] + data
    for d in data[row_begin]:
        answer += d % row_begin
        
    for i in range(row_begin + 1, row_end + 1):
        S = 0
        for d in data[i]:
            S += d % i
        answer ^= S
    return answer