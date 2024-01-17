#!/usr/bin/python3
def pow(a, b):
    if b >= 0:
        result = 1
        for _ in range(b):
            result *= a
    else:
        result = 1.0
        for _ in range(abs(b)):
            result /= a
    return "{:.15e}".format(result)
