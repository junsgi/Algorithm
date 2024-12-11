def merge(left, right, arr):
    if left >= right: return
    mid = (left + right) // 2
    merge(left, mid, arr)
    merge(mid + 1, right, arr)
    temp = []
    p1, p2 = left, mid + 1
    while p1 <= mid and p2 <= right:
        if arr[p1] + arr[p2] < arr[p2] + arr[p1]:
            temp.append(arr[p1])
            p1 += 1
        else:
            temp.append(arr[p2])
            p2 += 1
    while p1 <= mid: 
        temp.append(arr[p1])
        p1 += 1
    while p2 <= right:
        temp.append(arr[p2])
        p2 += 1
    for i in range(len(temp)):
        arr[left + i] = temp[i]
def solution(s):
    answer = []
    for i in s:
        if len(i) <= 3:
            answer.append("".join(i))
        else:
            cnt = 0
            stk = []
            for j in i:
                if len(stk) < 2 or stk[-2] + stk[-1] + j != "110":
                    stk.append(j)
                else:
                    cnt += 1
                    stk.pop()
                    stk.pop()
            if len(stk) >= 3 and stk[-3] + stk[-2] + stk[-1] == "110":
                cnt += 1
                stk.pop()
                stk.pop()
                stk.pop()
            x110 = "110" * cnt
            t = ""
            while stk and stk[-1] != "0":
                t += stk.pop()
            
            answer.append("".join(stk) + x110 + t)
    return answer
