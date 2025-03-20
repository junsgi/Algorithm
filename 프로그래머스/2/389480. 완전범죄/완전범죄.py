cache = dict()
def memo(depth, a, b, info, n, m):
    if depth == len(info):
        return a
    key = f"{depth}-{a}-{b}"
    if key in cache:
        return cache[key]
    cache[key] = 999999
    if a + info[depth][0] < n:
        cache[key] = min(cache[key], memo(depth + 1, a + info[depth][0], b, info, n, m))
    if b + info[depth][1] < m:
        cache[key] = min(cache[key], memo(depth + 1, a, b + info[depth][1], info, n, m))
    return cache[key]
def solution(info, n, m):
    res = memo(0, 0, 0, info, n, m)
    return -1 if res == 999999 else res
