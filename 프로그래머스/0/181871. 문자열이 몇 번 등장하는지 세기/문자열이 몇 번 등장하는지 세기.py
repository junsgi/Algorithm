def solution(myString, pat):
    if len(pat) > len(myString): return 0
    answer = 0
    for i in range(len(pat), len(myString) + 1):
        if myString[i - len(pat):i] == pat:
            answer += 1
    return answer