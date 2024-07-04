def solution(A, B):
    answer = 0
    i, j = 0, 0
    A.sort()
    B.sort()
    while j < len(B):
        if A[i] < B[j]:
            answer += 1
            i += 1
            j += 1
        else:
            while j < len(B) and A[i] >= B[j]:
                j += 1
            
                
    return answer