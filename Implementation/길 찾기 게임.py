# https://school.programmers.co.kr/learn/courses/30/lessons/42892
from collections import deque
import sys
sys.setrecursionlimit(10000)
class Node:
    def __init__(self, value : int, limit : int, left : object, right : object):
        self.value = value
        self.limit = limit
        self.left = left
        self.right = right
        
def checkTree(arr, st, ed):
    if st > ed: return False
    LENGTH = len(arr)
    for _ in range(LENGTH):
        num = arr.popleft()
        arr.append(num)
        if st < num < ed :
            return False
    return True
pre = []
post = []

def search(node, arr):
    if node == None:return

    # 전위 탐색
    pre.append(node.value)
    
    L = []
    R = []
    for v in arr:
        if node.limit < v[0]:
            R.append(v)
        else:
            L.append(v)
    if L:
        node.left = Node(L[0][2], L[0][0], None, None)
    if R:
        node.right = Node(R[0][2], R[0][0], None, None)

    search(node.left, L[1:])
    search(node.right, R[1:])
    
    # 후위 탐색
    post.append(node.value)

def solution(nodeinfo):
    # y 내림차순 : 0번째가 가장 위쪽에 위치
    # x는 y가 같다면 오름차순
    LEN = len(nodeinfo)
    print(LEN)
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)    
    nodeinfo.sort(key = lambda x : (-x[1], x[0]))
    # 시간 초과 주범
    root = Node(nodeinfo[0][2], nodeinfo[0][0], None, None)

    search(root, nodeinfo[1:])
    return [pre, post]
print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))
# [8, 6], [3, 5], [11, 5], [1, 3], [5, 3], [13, 3], [2, 2], [7, 2], [6, 1]
# [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]



"""
# https://school.programmers.co.kr/learn/courses/30/lessons/42892
from collections import deque
import sys
sys.setrecursionlimit(10000)
class Node:
    def __init__(self, value : int, limit : int, left : object, right : object):
        self.value = value
        self.limit = limit
        self.left = left
        self.right = right
        
def checkTree(arr, st, ed):
    if st > ed: return False
    LENGTH = len(arr)
    for _ in range(LENGTH):
        num = arr.popleft()
        arr.append(num)
        if st < num < ed :
            return False
    return True
pre = []
post = []

def search(node):
    if node == None:return
    # 전위 탐색
    pre.append(node.value)
    
    search(node.left)
    search(node.right)
    
    # 후위 탐색
    post.append(node.value)

def solution(nodeinfo):
    # y 내림차순 : 0번째가 가장 위쪽에 위치
    # x는 y가 같다면 오름차순
    LEN = len(nodeinfo)
    print(LEN)
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)    
    nodeinfo.sort(key = lambda x : (-x[1], x[0]))
    visit = [0] * (LEN)
    
    # 시간 초과 주범
    check = deque()
    root = Node(nodeinfo[0][2], nodeinfo[0][0], None, None)
    que = deque()
    que.append(root)
    visit[0] = 1
    check.append(root.limit)
    idx = 1
    while que :
        PARENT = que.popleft()
        for i in range(idx, LEN):

            # 왼쪽 자식, 좌에서 우로 가면서 확인
            if PARENT.left == None and not visit[i] and checkTree(check, nodeinfo[i][0], PARENT.limit):
                visit[i] = 1
                PARENT.left = Node(nodeinfo[i][2], nodeinfo[i][0], None, None)
                check.append(nodeinfo[i][0])
                que.append(PARENT.left)
                idx = i
                continue

            # 오른쪽 자식, 우에서 좌로
            if PARENT.right == None and not visit[i] and checkTree(check, PARENT.limit, nodeinfo[i][0]):
                visit[i] = 1
                check.append(nodeinfo[i][0])
                PARENT.right = Node(nodeinfo[i][2], nodeinfo[i][0], None, None)
                que.append(PARENT.right)
                idx = i + 1
                break
        #else:
            #idx += 1
    search(root)
    return [pre, post]


"""