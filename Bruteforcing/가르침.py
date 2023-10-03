# https://www.acmicpc.net/problem/1062
def func(depth, idx):
    global K, ans
    if depth == K:
        result = 0
        for word in words:
            cnt = 0            
            for w in word:
                if check[ord(w) - 97] == 1:
                    cnt += 1
                else:
                    break
            if cnt == len(word):
                result += 1
        ans = max(result, ans)
        return
    for i in range(idx, 26):
        if check[i] == 1: continue
        check[i] = 1
        func(depth + 1, i + 1)
        check[i] = 0

N, K = map(int, input().split())
check = [0] * 26
words = []
for _ in range(N):
    w = input()
    words.append(w[4:len(w) - 4])
if K < 5:
    print(0)
    exit()
ans = 0
check[ord('a') - 97] = 1
check[ord('c') - 97] = 1
check[ord('i') - 97] = 1
check[ord('n') - 97] = 1
check[ord('t') - 97] = 1
K -= 5
func(0, 0)
print(ans)
# antatica
# a, c, i, n, t 최소 5글자 이상
