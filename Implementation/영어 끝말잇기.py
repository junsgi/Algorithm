# https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    check = set()
    check.add(words[0])
    cnt = 2
    for i in range(1, len(words)):
        st, ed = words[i - 1], words[i]
        if st[-1] != ed[0] or ed in check:
            return [cnt % n if cnt % n else n, cnt // n + 1 if cnt % n else 0]
        check.add(ed)
        cnt += 1
    return [0, 0]
