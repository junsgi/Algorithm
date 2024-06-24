def solution(elements):
    ck = set()
    ck.add(sum(elements))
    LEN = len(elements)
    arr = [0] + elements + elements
    for i in range(1, LEN + LEN):
        arr[i] += arr[i - 1]
    for i in range(1, LEN + 1):
        for j in range(i, i + LEN):
            ck.add(arr[j] - arr[i - 1])
    return len(ck)