import math
MOD = 10**9+7


def dearengments(n, c = MOD):
    res = [1, 0]+[-1]*(n-1)


    for i in range(2, n+1):
        res[i] = (((i-1)%c)*(res[i-1] + res[i-2]) % c) % c

    return res[n]


print(dearengments(int(input())))



