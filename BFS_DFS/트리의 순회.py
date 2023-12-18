# https://www.acmicpc.net/problem/2263
import sys
sys.setrecursionlimit(100_000)
"""
후위 탐색 결과의 특정 구간중 가장 오른쪽 노드(요소)가 서브트리의 루트 노드임

# left
inSt = iS                   -> inOrder 리스트의 시작 주소

inEd = inOrderInfo[node]    -> inOrder 리스트의 끝 주소

LEN = inEd - inSt           -> 서브트리의 왼쪽 자식의 수

postSt = pS                 -> postOrder 리스트의 시작 주소

postEd = postSt + LEN - 1   -> postOrder 리스트의 끝 주소 - 1

==================================================================

#right
inSt = inEd + 1                     -> inOrder 리스트의 끝 주소 + 1

inEd = iE                           -> 현재 재귀 구간의 inOrder 리스트 전체 길이

LEN = inEd - inSt                   -> 서브트리의 오른쪽 자식의 수

postSt = postEd + 1                 -> 왼쪽 서브트리의 루트 노드 인덱스 + 1

postEd = postOrderInfo[node] - 1    -> 루트노드 인덱스 - 1
"""
def DIV(node, pS, pE, iS, iE):

    if node in check:
        return
    print(node, end = ' ')
    check.add(node)
    if pE - pS <= 0: return

    # left
    inSt = iS
    inEd = inOrderInfo[node]
    LEN = inEd - inSt

    postSt = pS
    postEd = postSt + LEN - 1

    DIV(postOrder[postEd], postSt, postEd, inSt, inEd)


    #right
    inSt = inEd + 1
    inEd = iE

    LEN = inEd - inSt

    postSt = postEd + 1
    postEd = postOrderInfo[node] - 1

    DIV(postOrder[postEd], postSt, postEd, inSt, inEd)


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
DIV(root, 0, n, 0, n)
"""
7
3 2 5 4 1 6 7
3 5 4 2 7 6 1

1 2 3 4 5 6 7

9
2 1 4 6 3 9 7 5 8
2 6 4 9 7 8 5 3 1

1 2 3 4 6 5 7 9 8
"""