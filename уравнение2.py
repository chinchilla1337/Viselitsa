for b in range(1, 10):
    for k in range(1, 20):
        for t in range(1, 200):
            if 10 * b + k * 5 + 0.5 * t == 100 and b + k + t == 100:
                print(b, k, t)
