a = int(input())
cnt = 0
while a >= 25:
    cnt = cnt + 1 * (a // 25)
    a = a % 25
while a >= 10:
    cnt = cnt + 1 * (a // 10)
    a = a % 10
while a >= 5:
    cnt = cnt + 1 * (a // 5)
    a = a % 5
while a >= 1:
    cnt = cnt + a
    a = a % 1
print(cnt)
