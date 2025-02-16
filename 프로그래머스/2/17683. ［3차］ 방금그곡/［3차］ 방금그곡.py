def ttos(s):
    return int(s[:2]) * 60 + int(s[3:])
def p(s):
    stk = []
    for i in s:
        if "A" <= i and i <= "G":
            stk.append(i)
        else:
            stk[-1] = stk[-1].lower()
    return "".join(stk)
def solution(m, musicinfos):
    answer = '(None)'
    check1 = -1
    check2 = 0x7fffffff
    m = p(m)
    for x in range(len(musicinfos)):
        music = musicinfos[x]
        start, end, title, melody = music.split(",")
        start, end = ttos(start), ttos(end)
        if (end - start) < len(m): continue
        melody = p(melody)
        if end - start < len(melody):
            melody = melody[:end - start]
            if m in melody and (check1 < (end - start) or (check1 == (end - start) and check2 > x)):
                check1 = (end - start)
                check2 = x
                answer = title
        else:
            for i in range(len(melody)):
                if melody[i] != m[0]: continue
                hit = False
                ck = True
                for j in range(i, i + (end - start) + 1):
                    if j - i == len(m):
                        hit = True
                        break
                    if melody[j % len(melody)] != m[j - i]:
                        ck = False
                        break
                if (hit or ck) and (check1 < (end - start) or (check1 == (end - start) and check2 > x)):
                    check1 = (end - start)
                    check2 = x
                    answer = title
    return answer