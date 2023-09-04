"""
브루트포트 문제이기도 하지면 수학 문제 풀듯 풀었다.

1. 길이가 1
    - 무수히 많음 A

    길이가 2
    - 두 개의 원소가 같다면 a = 1, b = 0이므로 똑같이 출력
    - 다르다면 무수히 많으므로 A

    길이가 3이상
    - 3이상이지만 맨 앞 두 원소가 같은지 같지 않은지 체크
        *) 같으면 뒤에 0으로 나누게 되므로 위와같이 처리

          A1 * a + b = A2
        - A2 * a + b = A3
    a = (A3 - A2) / (A2 - A1)
    b = -( A1 * a - A2)

    나머지 요소에 수식을 적용했을 때 다른 요소가 나온다면 구할 수 없기 때문에 B
    모두 맞다면 출력
"""
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

