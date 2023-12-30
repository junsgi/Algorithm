import sys
input = sys.stdin.readline
def up(idx):
    if idx // 2 == 0: return
    if heap[idx] < heap[idx // 2]:
        heap[idx], heap[idx // 2] = heap[idx // 2], heap[idx]
        up(idx // 2)

def down(idx):
    global length
    tx = idx * 2
    if tx > length: return
    if tx + 1 <= length and heap[tx] > heap[tx + 1]: tx += 1
    if heap[idx] > heap[tx]:
        heap[idx], heap[tx] = heap[tx], heap[idx]
        down(tx)

n = int(input())
heap = [0] * (n + 1)
length = 0
for _ in range(n):
    t = int(input())

    if not t:
        if not length:
            print(0)
        else:
            print(heap[1])
            heap[1] = heap[length]
            length -= 1
            down(1)
    else:
        length += 1
        heap[length] = t
        up(length)