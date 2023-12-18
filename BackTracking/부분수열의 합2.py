# https://www.acmicpc.net/problem/1208
n, target = map(int, input().split())
arr = list(map(int, input().split()))
temp = []
check = set()
answer = 0
def BACK(idx, end, res, status):
    global answer, n, target
    if idx == end:
        if status:
            temp.append(res)
        elif not status:
            le = 0
            ri = len(temp) - 1
            while le <= ri:
                mid = (le + ri) // 2
                t = temp[mid] + res
                if t < target:
                    le = mid + 1
                elif target < t:
                    ri = mid - 1
                else:
                    answer += 1
                    break
        return
    BACK(idx + 1, end, res + arr[idx], status)
    BACK(idx + 1, end, res, status)

BACK(0, n // 2, 0, True)
temp.sort()
BACK(n // 2, n, 0, False)
if answer - 1 < 0: print(0)
else: print(answer - 1)
