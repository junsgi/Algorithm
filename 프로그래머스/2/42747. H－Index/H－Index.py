def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)
    for i in range(citations[-1] + 1):
        j = -1
        for j in range(n):
            if i <= citations[j]:
                break
        if n - j >= i and j <= i:
            answer = max(answer, i)
                
        
    
        
    return answer