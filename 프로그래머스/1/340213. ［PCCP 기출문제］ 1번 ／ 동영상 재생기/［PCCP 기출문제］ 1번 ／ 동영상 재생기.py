def stoi(string):
    h, s = map(int, string.split(":"))
    return h * 60 + s
def itos(i):
    return "%02d:%02d" % (i // 60, i % 60)
def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    LEN = stoi(video_len)
    pos = stoi(pos)
    start = stoi(op_start)
    end = stoi(op_end)
    if start <= pos <= end:
        pos = end
    for c in commands:
        if c == "next":
            pos += 10
        else:
            pos -= 10
        if pos > LEN:
            pos = LEN
        if pos < 0:
            pos = 0
        if start <= pos <= end:
            pos = end
    return itos(pos)