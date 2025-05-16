import sys
input = sys.stdin.readline
def fibo(num):
	if arr[num]:
		return arr[num]
	if num <= 0 : return 0
	if num == 1 : return 1

	arr[num] = fibo(num - 1) + fibo(num - 2)
	zero[num] = zero[num - 1] + zero[num - 2]
	one[num] = one[num - 1] + one[num - 2]
	return arr[num]

arr = [0] * 50
zero = [0] * 50
one = [0] * 50
zero[0] = one[1] = 1
n = int(input())
for _ in range(n) :
	t = int(input())
	fibo(t)
	print(zero[t], one[t])