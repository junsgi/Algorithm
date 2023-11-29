# https://www.acmicpc.net/problem/5639
import sys
sys.setrecursionlimit(10000)
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def pro(node, value):
    if node.value < value:
        if node.right == None:
            node.right = Node(value)
            return
        else:
            return pro(node.right, value)
    else:
        if node.left == None:
            node.left = Node(value)
            return
        else:
            return pro(node.left, value)
def post(node):
    if not node : return
    post(node.left)
    post(node.right)
    print(node.value)

root = None
while True: # 입력 제한이 없다.
    try:
        n = (int(sys.stdin.readline()))
        if root == None:
            root = Node(n)
        else:
            pro(root, n)
    except:
        break

post(root)