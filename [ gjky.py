n = int(input())
a = ""
mx = ""
cnt = 0
for i in range(n):
    s = input()
    a = s[: s.find(" ")] + s[s.find("«") + 1 : s.find("»")]
    b = a
    if b >= mx:
        mx = b
        cnt += 1
if cnt == n:
    print("YES")
else:
    print("NO")
