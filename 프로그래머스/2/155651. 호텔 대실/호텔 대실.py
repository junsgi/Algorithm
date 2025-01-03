def stoi(s):
    x, y = map(int, s.split(":"))
    return x * 60 + y
def solution(book_time):
    answer = 1
    arr = []
    for a, b in book_time:
        a = stoi(a)
        b = stoi(b) + 10
        arr.append((a, 1))
        arr.append((b, -1))
    arr.sort()
    s = 1
    for i in range(1, len(arr)):
        s += arr[i][1]
        answer = max(answer, s)
    return answer