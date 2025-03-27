def p(n):
    arr = []
    for i in range(1, n + 1):
        if n % i == 0:
            arr.append(i)
    return arr;
def solution(brown, yellow):
    arr = p(brown + yellow)
    for i in range(len(arr)):
        width = arr[i]
        height = arr[len(arr) - i - 1]
        if width - 2 < 0: continue
        if (width - 2) * (height - 2) == yellow:
            return [height, width]
