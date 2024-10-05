import math
import cProfile
from sys import stdin
MAX_B = 10**9
MOD = 10**9+7

def _bin_fme(a, b, c = MOD):
    n = math.ceil(math.log2(b+1))

    bins = []
    pows = [a] + n*[0]
    res = 1

    for pos, bit in enumerate(reversed(bin(b)[2:])): 
        if bit == '1':
            bins.append(pos)
    
    for i in range(1, n+1): #b+1 ensures log domain
        pows[i]=((pows[i-1] ** 2) % MOD)


    for i in bins:
        res *= pows[i]
        res %= MOD
    return res 

    
def bin_fme(max = MAX_B):

    data = [line.rstrip() for line in stdin.readlines()]
    n = int(data[0])
    for i in data[1:]:
        a, b =[int(x) for x in i.split()]
        print(_bin_fme(a, b))



    
def main():
    bin_fme()

 
main()

