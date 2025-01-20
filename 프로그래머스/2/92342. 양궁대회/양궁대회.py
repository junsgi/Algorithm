
def solution(n, info):
    answer = [0] * 11
    arr = [0] * 11
    score = 0
    def check():
        nonlocal arr, answer
        for i in range(10, -1, -1):
            if arr[i] > answer[i]:
                return True
            elif arr[i] < answer[i]:
                return False
        return False
    def d(depth, idx, A, B):
        nonlocal score, arr, answer
        if depth < 0: return
        if idx == 11:
            if depth != 0 or A <= B: 
                return
            if score < A - B or (score == A - B and check()):
                answer = arr[:]
                score = A - B
            return
        for i in range(info[idx] + 2):
            arr[idx] = i
            ta = A + ((10 - idx) if i > info[idx] else 0)
            tb = B + ((10 - idx) if info[idx] != 0 and arr[idx] <= info[idx] else 0)
            d(depth - i, idx + 1, ta, tb)
            arr[idx] = 0
    d(n, 0, 0, 0)
    if score == 0: answer = [-1]
    return answer