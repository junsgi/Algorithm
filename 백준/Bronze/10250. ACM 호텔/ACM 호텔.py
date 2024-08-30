num = int(input())

while num:
    H, W, N = map(int,input().split())
    one = 1
    if N > H:
        while N > H:
            N -= H
            Ten_room = N
            one += 1
    else:
        Ten_room = N
    

    if one < 10:
        print(str(Ten_room)+'0'+str(one))
    else:
        print(str(Ten_room)+str(one))
    num -= 1