# https://www.acmicpc.net/problem/1700
import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.freq = 0
        self.age = 0
        self.status = False

n, m = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
plug = [Node() for _ in range(101)]
used = []
for i in arr: 
    plug[i].freq += 1

idx = 0
cnt = 0
# 처음에 꼽을 수 있는 만큼 꼽는다.
while idx < m and cnt != n:
    if not plug[arr[idx]].status:
        plug[arr[idx]].status = True
        cnt += 1
        used.append(arr[idx])
    plug[arr[idx]].freq -= 1 
    idx += 1
answer = 0

for i in range(idx, m):
    # 만약 꼽혀있다면 
    if plug[arr[i]].status :
        plug[arr[i]].freq -= 1
    else:
        answer += 1
        fidx = -1
        FLAG = False

        fidx = -1
        for j in range(n):
            if plug[used[j]].freq <= 0:
                fidx = j
                FLAG = True
                break
            for k in range(i + 1, m):
                if used[j] == arr[k]:
                    fidx = max(fidx, k)
                    break
        if not FLAG:
            fidx = used.index(arr[fidx])
            
        plug[used[fidx]].status = False
        used[fidx] = arr[i]
        plug[used[fidx]].status = True
        plug[used[fidx]].freq -= 1

print(answer)