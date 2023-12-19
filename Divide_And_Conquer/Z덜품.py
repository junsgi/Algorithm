# https://www.acmicpc.net/problem/1074
import sys
sys.setrecursionlimit(2 ** 14)
n, r, c = map(int, input().split())
swi = False
answer = 0
def rec(x, y, size):
    global r, c, answer, swi
    if x == r and y == c or swi: 
        print(answer)
        print(2 ** 15)
        exit()
    if size == 1:
        answer += 1
        return
    rec(x, y, size // 4)
    rec(x, y + int(size ** 0.5) // 2, size // 4)
    rec(x + int(size ** 0.5) // 2, y, size // 4)
    rec(x + int(size ** 0.5) // 2, y + int(size ** 0.5) // 2, size // 4)
rec(0, 0, 4 ** n)
