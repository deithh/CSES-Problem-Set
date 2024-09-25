from collections import Counter
from functools import lru_cache
 
MODVAL = 10**9 + 7

@lru_cache(maxsize=2**18)
def fme(a, b, c = 10**9 + 7):
    if b == 0:
        return 1
    if b % 2 == 0:
        return ((fme(a, b/2) %c)*(fme(a, b/2)%c)) % c
    else:
        b-=1
        return ((fme(a, b/2) %c)*(fme(a, b/2)%c)* a %c) % c

@lru_cache
def modfac(n, c = MODVAL):
    result = 1
    if n == 1:
        return result
    for i in range(2, n+1):
        result = result * i % c
    return result

#since modval is prime modinv using fermat little theorem
def modinv(a, c= MODVAL):
    return fme(a, c-2, c)
    

seq = input()
C = Counter(seq)
res = modfac(len(seq))
for i in C.values():
    if i>1:
        res = res * modinv(modfac(i)) % MODVAL

print(res)

