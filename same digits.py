import math

a = int(input())
if (a // (a % 10) * 9 + 1) % (10 ** int(math.log10(a))) == 0:
    print("YES")
else:
    print("NO")
