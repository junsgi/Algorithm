from collections import defaultdict
def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    s1, s2 = defaultdict(int), defaultdict(int)
    for i in range(1, len(str1)):
        temp = str1[i - 1 : i + 1]
        for s in temp:
            if not ('a' <= s <= 'z'):
                break
        else:
            s1[temp] += 1
    for i in range(1, len(str2)):
        temp = str2[i - 1 : i + 1]
        for s in temp:
            if not ('a' <= s <= 'z'):
                break
        else:
            s2[temp] += 1
    union = 0
    intersection = 0
    s1Items = s1.items()
    s2Items = s2.items()
    for s, c in s1Items:
        if s in s2: 
            intersection += min(c, s2[s])
            union += max(c, s2[s])
        else : union += c
    for s, c in s2Items:
        if s not in s1: union += c
    answer = 65536
    if union:
        answer *= intersection / union
    return int(answer)