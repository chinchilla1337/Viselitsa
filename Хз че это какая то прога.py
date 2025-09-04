a, b = int(input()), int(input())
if a == 1:
    for i in range(a + 1, b + 1):
        cnt = 0
        for j in range(2, i):
            if i % j == 0:
                cnt += 1
        if cnt == 0:
            print(i)
else:
    for i in range(a, b + 1):
        cnt = 0
        for j in range(2, i):
            if i % j == 0:
                cnt += 1
        if cnt == 0:
            print(i)
