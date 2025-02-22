def two(n):
    while n:
        if n % 10 == 2:
            return False
        n //= 10
    return True
def solution(arr):
    idx1 = 0
    idx2 = len(arr)-1
    while idx1 < len(arr) and two(arr[idx1]):
        idx1+=1
    while 0 < idx2 and two(arr[idx2]):
        idx2-=1
    if idx1 > idx2: return [-1]
    return arr[idx1:idx2+1]