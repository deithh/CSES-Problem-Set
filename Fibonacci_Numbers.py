from functools import lru_cache
 
MODVAL = 10**9 + 7

@lru_cache(maxsize=2**18)
def modfibo(n):
    if n == 2:
        return 1
    if n == 1:
        return 1
    if n == 0:
        return 0
    
    if n % 2 == 1:
        return ((modfibo((n+1)//2 - 1))**2  + (modfibo((n+1)//2))**2) % MODVAL
    else:
        return ((2*modfibo(n//2 + 1) - modfibo(n//2)) * modfibo(n//2)) % MODVAL


n = int(input())
print(modfibo(n))