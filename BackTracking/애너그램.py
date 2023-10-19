# https://www.acmicpc.net/problem/6443
import sys
input = sys.stdin.readline
n = int(input())
words = [list(input().strip()) for _ in range(n)]
def BACK(check : dict, value, limit):
    if len(value) == limit:
        print(value)
        return

    for i in check.keys():
        if not check[i]: continue
        check[i] -= 1
        BACK(check, value + i, limit)
        check[i] += 1

visit = set()
answer = ''
for w in words:
    check = {}
    for s in sorted(w):
        if s in check: check[s] += 1
        else: check[s] = 1
    BACK(check, "", len(w))

# 1차원 체크 배열을 사용하니 시간초과 (자릿수는 길고 idx는 0부터 돌아서 그런듯)
# 딕셔너리를 이용해 알파벳 개수를 세는 방식으로 해결