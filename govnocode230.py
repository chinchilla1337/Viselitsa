import time
import math


start_time = time.time()


def minimal_iterations(opers, start, finish):
    k = 0
    knums = [start]
    donenums = {start: None}

    while True:
        num = knums.pop(0)
        for oper in opers:
            n = oper(num)
            if n not in donenums:
                knums.append(n)
                donenums[n] = num
                if n == finish:
                    res = [n]
                    while res[-1] != None:
                        res.append(donenums[res[-1]])
                    res.pop()
                    return list(reversed(res))
        if len(knums) % 1000 == 0:
            print(f"{len(donenums)}")


def mult_by_2(x):
    return x * 2


def subtract_by_3(x):
    return x - 3


print(minimal_iterations([mult_by_2, subtract_by_3], 1, 100000))

print(f"Elapsed time: {time.time() - start_time:.4f} seconds")
