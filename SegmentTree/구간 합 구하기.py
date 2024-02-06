def insert(left, right, idx):
    mid = (left + right) // 2
    if left == right :
        seg[idx] = num[left]
        return seg[idx]
    seg[idx] = insert(left, mid, idx * 2) + insert(mid + 1, right, idx * 2 + 1)
    return seg[idx]
def update(left, right, idx):
    global a, b, c
    mid = (left + right) // 2
    if b < left or right < b: return seg[idx]
    if left == b and right == b:
        seg[idx] = c
        return seg[idx]
    seg[idx] = update(left, mid, idx * 2) + update(mid + 1, right, idx * 2 + 1)
    return seg[idx]
def get(left, right, idx):
    global a, b, c
    mid = (left + right) // 2
    if c < left or right < b : return 0
    if b <= left and right <= c: return seg[idx]
    return get(left, mid, idx * 2) + get(mid + 1, right, idx * 2 + 1)
n, m, k = map(int, input().split())
num = [0]
seg = [0] * (1 << 21)
for _ in range(n):
    num.append(int(input()))
insert(1, n, 1)
a = b = c = 0
for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a & (1 << 0):
        update(1, n, 1)
    else:
        print(get(1, n, 1))