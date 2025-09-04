from math import *

m, n = int(input()), int(input())
if m != n:
    p = n - m
    x = p / abs(p)
    x = int(x)
    for i in range(m, n + x, x):
        print(i)
else:
    print(m)
