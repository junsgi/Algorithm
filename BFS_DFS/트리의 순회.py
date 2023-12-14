# https://www.acmicpc.net/problem/2263
import sys
sys.setrecursionlimit(100_000)
def DIV(node, start, end):
    global n
    
    if node in check or end - abs(start) <= 0:
        return

    print(node, end = ' ')
    check.add(node)
    
    newLeftLength = inOrderInfo[node] - start
    DIV(postOrder[newLeftLength - 1], start, newLeftLength + 1)

    newRightLength = end - (newLeftLength + 1)
    DIV(postOrder[postOrderInfo[node] - 1], newLeftLength + 1, newLeftLength + newRightLength)

n = int(input())
inOrderInfo = {}
postOrderInfo = {}
check = set()
inOrder = list(map(int, input().split()))
postOrder = list(map(int, input().split()))
for i in range(n):
    inOrderInfo[inOrder[i]] = i
    postOrderInfo[postOrder[i]] = i
root = postOrder[-1]
DIV(root, 0, n - 1)
"""
7
3 2 5 4 1 6 7
3 5 4 2 7 6 1

1 2 3 4 5 6 7

9
2 1 4 6 3 9 7 5 8
2 6 4 9 7 8 5 3 1

1 2 3 6 4 5 7 9 8
"""