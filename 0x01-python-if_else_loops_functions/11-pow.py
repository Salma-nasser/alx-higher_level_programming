#!/usr/bin/python3
def pow(a, b):
    if b >= 0:
        result = 1
        for _ in range(b):
            result *= a
        return result
    else:
        result = 1.0
        for _ in range(abs(b)):
            result /= a
        if -0.001 < result < 0.001:
            return "{:.15e}".format(result)
        else:
            return "{:.2f}".format(result)
