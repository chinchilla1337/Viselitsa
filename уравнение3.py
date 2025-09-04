s = 0
for a in range(1, 151):
    for b in range(1, 151):
        for c in range(1, 151):
            for d in range(1, 151):
                for e in range(1, 151):
                    if a**5 + b**5 + c**5 + d**5 == e**5:
                        s = a + b + c + d + e
                        break
    if s != 0:
        break