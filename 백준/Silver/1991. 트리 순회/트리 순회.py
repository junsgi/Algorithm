
class Node:
  def __init__(self, value):
    self.value=chr(value)
    self.left=None
    self.right=None
a1 = ["","",""]
def pro(n):
  if n == None : return
  a1[0] += n.value
  pro(n.left)
  a1[1] += n.value
  pro(n.right)
  a1[2] += n.value

n = int(input())
arr = [Node(i+65) for i in range(n)]
for _ in range(n):
  a, b, c = input().split()
  if b !=".":
    arr[ord(a)-65].left = arr[ord(b)-65]
  if c !=".":
    arr[ord(a)-65].right = arr[ord(c)-65]
pro(arr[0])
for i in a1:
  print(i)