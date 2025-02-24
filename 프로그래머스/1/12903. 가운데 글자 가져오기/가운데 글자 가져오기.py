def solution(s):
    return s[len(s)>>1] if len(s)&1 else s[(len(s)>>1)-1:(len(s)>>1)+1]