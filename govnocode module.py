n = int(input())
s = 0
while n > 0:
    ld = n % 10
    s += ld
    n //= 10
while s > 9:
    k = 0
    while s > 0:
        ld2 = s % 10
        k += ld2
        s //= 10
    s = k
print(s)
  # более простой и предпочтительный варик:
n = int(input())
while n>9:
    k=0
    while n>0:
        ld=n%10
        k+=ld
        n//=10
    n=k
print(n)
