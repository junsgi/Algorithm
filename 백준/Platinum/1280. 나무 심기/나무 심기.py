# (x - a) + (x - b) + (x - c)
# x * n + (-a + -b + -c)
# x * n - (a + b + c)
# 세그먼트 트리에 각 요소의 값과 개수를 저장한다
import sys
input = sys.stdin.readline
def insert(left, right, idx, value):
    global seg
    if value < left or right < value: 
        return seg[idx]
    if value == left and value == right:
        seg[idx][0] += value
        seg[idx][1] += 1
        return seg[idx]
    mid = (left + right) // 2
    l = insert(left, mid, idx * 2, value) 
    r = insert(mid + 1, right, idx * 2 + 1, value)
    seg[idx][0] = l[0] + r[0]
    seg[idx][1] = l[1] + r[1]
    return seg[idx]
def query(left, right, idx, st, ed):
    global seg
    if ed < left or right < st:
        return 0, 0
    if st <= left and right <= ed:
        return seg[idx]
    mid = (left + right) // 2
    l = query(left, mid, idx * 2, st, ed)
    r = query(mid + 1, right, idx * 2 + 1, st, ed)
    return l[0] + r[0], l[1] + r[1]
n = int(input().strip())
arr = []
for _ in range(n):
    arr.append(int(input().strip()) + 1)

MAX = max(arr)
MOD = 1_000_000_007
answer = 1
LEN = 1
cnt = 1
while LEN <= MAX:
    LEN *= 2
    cnt += 1

seg = [[0, 0] for _ in range(1 << cnt)]
insert(1, LEN, 1, arr[0])
for i in range(1, n):
    left = query(1, LEN, 1, 1, arr[i] - 1)
    l = arr[i] * left[1] - left[0]

    right = query(1, LEN, 1, arr[i] + 1, MAX)
    r = right[0] - (arr[i] * right[1])

    insert(1, LEN, 1, arr[i])
    answer *= l + r
    answer %= MOD
print(answer)
