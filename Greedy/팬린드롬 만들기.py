word = input()
check = {}
for i in word:
    if i in check:
        check[i] += 1
    else:      
        check[i] = 1
check = dict(sorted(check.items(), key = lambda x : (x[0], -x[1])))
ans = ""
for char, cnt in check.items():
    ans += char * (cnt // 2)
    check[char] -= cnt // 2
    
if len(word) % 2 :
    ans += "0" + ans[::-1]
else:
    ans += ans[::-1]


for i in ans[len(ans): len(ans) // 2: -1]:
    if i not in check:
        print("I'm Sorry Hansoo")
        exit()
    check[i] -= 1
    if check[i] == 0:
        check.pop(i)


if len(word) % 2:
    ans = ans.replace("0", list(check.keys())[0])

if len(ans) != len(word):
    print("I'm Sorry Hansoo")
else:
    print(ans)