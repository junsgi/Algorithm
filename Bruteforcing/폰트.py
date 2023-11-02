# https://www.acmicpc.net/problem/9997
import sys
input = sys.stdin.readline
def wordProc(w):
    result = 0
    check.clear()
    for i in w:
        if i not in check:
            result = result | (1 << (ord(i) - 97))
        check.add(i)
    return result


def solution(idx, value):
    global n, answer

    # 2 ^ 26 - 1 = 67108863  A = 1
    if value == 67108863:
        answer += 1
    
    for i in range(idx, n): # 브루트 포스 코드
        solution(i + 1, value | word[i])

n = int(input())
word = [input().strip() for _ in range(n)]
check = set()
answer = 0
for i in range(n):
    word[i] = wordProc(word[i])
solution(0, 0)
print(answer)

"""
a = 0b1
b = 0b10
c = 0b100
d = 0b1000
...
z = ob10^25

11 1111 1111 1111 1111 1111 1111 : 1이 26개면 모든 알파벳을 사용한 것임
10진수로 바꾸면 67,108,863
"""