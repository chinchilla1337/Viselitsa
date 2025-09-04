n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    else:
        for q in range(i - 1, 0, -1):
            print(q, end="")
    print()
