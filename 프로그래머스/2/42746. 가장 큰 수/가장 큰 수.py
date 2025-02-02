temp = [None] * 100000
def sort(left, right, arr):
    mid = (left + right) // 2
    l = left
    r = mid + 1
    idx = 0
    while l <= mid and r <= right:
        a, b = arr[l], arr[r]
        if a + b < b + a:
            temp[idx] = b
            r += 1
        else:
            temp[idx] = a
            l += 1
        idx += 1
    while l <= mid:
        temp[idx] = arr[l]
        l += 1
        idx += 1
    while r <= right:
        temp[idx] = arr[r]
        r += 1
        idx += 1
    for i in range(idx):
        arr[left + i] = temp[i]
def merge(left, right, arr):
    if left >= right: return
    mid = (left + right) // 2
    merge(left, mid, arr)
    merge(mid + 1, right, arr)
    sort(left, right, arr)
    
def solution(numbers):
    numbers = list(map(str, numbers))
    merge(0, len(numbers) - 1, numbers)
    answer = ''.join(numbers)
    if answer.count("0") == len(answer):
        return "0"
    return answer