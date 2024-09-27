n = int(input())
arr = list(map(int, input().split()))
if n == 1 or n == 2:
    if n == 1:
        print('A')
    elif n == 2 and arr[0] == arr[1]:
        print(arr[1])
    else:
        print("A")
    exit()
else:
    if arr[0] == arr[1]:
        for i in range(2, n):
            if arr[i - 1] != arr[i]:
                print("B")
                exit()
        print(arr[0])
    else:
        mul = (arr[2] - arr[1]) // (arr[1] - arr[0])
        plus = -(arr[0] * mul - arr[1])
        for i in range(1, n):
            if arr[i] != arr[i-1] * mul + plus:
                print("B")
                exit()
        print(arr[-1] * mul + plus)