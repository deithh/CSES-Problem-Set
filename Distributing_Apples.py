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
    

n, m = [int(x) for x in input().split()]

result = modfac(n+m-1)
result = result * modinv(modfac(n-1)) % MODVAL
result = result * modinv(modfac(m)) % MODVAL

print(result)