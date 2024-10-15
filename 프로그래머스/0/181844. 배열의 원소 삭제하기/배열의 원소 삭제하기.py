def solution(arr, delete_list):
    answer = []
    for i in delete_list:
        idx = -1
        for j in range(len(arr)):
            if arr[j] == i:
                idx = j
                arr[idx] = None
                idx += 1
                while idx < len(arr):
                    arr[idx - 1] = arr[idx]
                    idx += 1
                if idx == len(arr):
                    arr[idx - 1] = None
    i = 0
    while i < len(arr) and arr[i] != None:
        answer.append(arr[i])
        i += 1
    return answer