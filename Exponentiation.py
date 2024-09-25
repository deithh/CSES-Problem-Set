from functools import lru_cache
 
@lru_cache(maxsize=2**18)
def fme(a, b, c = 10**9+7):
    if b == 0:
        return 1
    if b % 2 == 0:
        return ((fme(a, b/2) %c)*(fme(a, b/2)%c)) % c
    else:
        b-=1
        return ((fme(a, b/2) %c)*(fme(a, b/2)%c)* a %c) % c
    
def main():
    n = int(input())
    for i in range(n):
        a, b =[int(x) for x in input().split()]
        print(fme(a, b))
 
 
if __name__ == '__main__':
    main()

# too slow