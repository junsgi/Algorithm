# https://www.acmicpc.net/problem/1074
n, r, c = map(int, input().split())
answer = 0
def rec(x, y, size, length):
    global r, c, answer
    if x == r and y == c: 
        print(answer)
        exit()
    if size == 1:
        return
    tSize = length // 2
    rec(x,         y,         size // 4)
    rec(x,         y + tSize, size // 4)
    rec(x + tSize, y,         size // 4)
    rec(x + tSize, y + tSize, size // 4)
rec(0, 0, 4 ** n, 2 ** n)
"""
한 변의 길이 (length) = 2 ** n 
x + length // 2, y + length // 2
x + length // 2, y + length
x + length, y + length // 2
x + length, y + length
"""
