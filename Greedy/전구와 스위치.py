# https://www.acmicpc.net/problem/2138
n = int(input())
bulb = list(input())
target = list(input())
def check(n):
  bulb_copy = bulb[:]
  cnt = 0
  for i in range(1, n):
    if bulb_copy[i - 1] != target[i - 1]:
      cnt += 1
      bulb_copy[i - 1] = '0' if bulb_copy[i - 1] == '1' else '1'
      bulb_copy[i] = '0' if bulb_copy[i] == '1' else '1'
      if i + 1 < n:
        bulb_copy[i + 1] = '0' if bulb_copy[i + 1] == '1' else '1'
    if bulb_copy == target:
      return cnt
  return 0x7fffffff
ans = check(n)
bulb[0] = '0' if bulb[0] == '1' else '1'
bulb[1] = '0' if bulb[1] == '1' else '1'
ans= min(ans, check(n)+1)
print(-1 if ans == 0x7fffffff else ans)
