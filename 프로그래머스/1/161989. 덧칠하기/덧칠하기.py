def solution(n, m, section):
    answer = 1
    start = section[0]
    idx = 1
    while idx < len(section):
        if start + m - 1 >= section[idx]:
            idx += 1
        else:
            start = section[idx]
            answer += 1
            idx += 1
    return answer