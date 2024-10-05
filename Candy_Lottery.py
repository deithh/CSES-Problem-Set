import math
from decimal import Decimal, getcontext
getcontext().prec = 10
def round_half_up(n, decimals=0):
    multiplier = 10**decimals
    return math.floor(n * multiplier + Decimal(0.5)) / multiplier

def solve(n, k):

    res = Decimal('0.0')
    memo = [0]
    for i in range(1, k+1):
        p = (Decimal(i)/Decimal(k)) ** Decimal(n) 
        memo.append(p)
        res += (p - memo[i-1])* Decimal(i)


    return res


n, k = [int(x) for x in input().split()]
res = round_half_up(solve(n, k),6)
print(f"{res:.6f}")