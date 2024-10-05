import sys
import math
MOD = 10**9 + 7
 
def bin_fme(a, b, c = MOD):
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

def modfac(n, c = MOD):
    result = [1, 1]
    if n == 1:
        return result
    for i in range(2, n+1):
        result.append(result[-1] * i % c)
    return result
 
#since modval is prime modinv using fermat little theorem
def modinv(a, c= MOD):
    return bin_fme(a, c-2, c)
    
def main():
    mfac = modfac(10**6)
    
    data = [x.rstrip() for x in sys.stdin.readlines()]
    n = int(data[0])
    for i in data[1:]:
        a, b = [int(x) for x in i.split()]
        res = mfac[a]
        res = res * modinv(mfac[b]) % MOD
        res = res * modinv(mfac[a-b]) % MOD
        print(res)


main()