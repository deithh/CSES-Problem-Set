import sys
def inv_sieve(n):
    cache = [0]*(n+1)
    for i in range(1, n+1):
        for j in range(i, n+1, i):
            cache[j] += 1

    return cache

data = [int(x.rstrip()) for x in sys.stdin.readlines()[1:]]
n = max(data)
cache = inv_sieve(n)
for i in data:
    a = int(i)
    print(cache[a])