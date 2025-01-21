from collections import defaultdict
def solution(info, query):
    answer = []
    dic = defaultdict(list)
    def p(idx, arr, res):
        if idx == 4:
            dic[res].append(int(arr[idx]))
            return
        p(idx + 1, arr, res + arr[idx])
        p(idx + 1, arr, res + "-")
    for i in info:
        p(0, i.split(), "")
    for k in dic.keys():
        dic[k].sort()
    for q in query:
        q = q.split()
        key = ""
        for i in range(0, 7, 2): key += q[i]
        k = int(q[-1])
        left = 0
        right = len(dic[key]) - 1
        mid = 0
        while left <= right:
            mid = (left + right) // 2
            if dic[key][mid] < k:
                left = mid + 1
            elif dic[key][mid] > k:
                right = mid - 1
            else:
                while mid - 1 >= 0 and dic[key][mid - 1] == k:
                    mid -= 1
                answer.append(len(dic[key]) - mid)
                break
        else:
            answer.append(len(dic[key]) - left)
    return answer