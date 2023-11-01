# https://www.acmicpc.net/problem/9997
n = int(input())
word = [input() for _ in range(n)]
visit = [0] * n
check = [0] * (26)
answer = 0
def wordProc(w):
    result = 0
    for i in w:
        if check[ord(i) - 97] == 0:
            check[ord(i) - 97] = 1
            result += 1
        else:
            check[ord(i) - 97] += 1
    return result

def BACK(w):
    for i in w:
        check[ord(i) - 97] -= 1

def solution(idx, value):
    global n, answer
    if value == 26:
        answer += 1
        return
    
    for i in range(idx, n):
        if visit[i]: continue
        visit[i] = 1
        solution(i, value + wordProc(word[i]))
        BACK(word[i])
        visit[i] = 0

solution(0, 0)
print(answer)