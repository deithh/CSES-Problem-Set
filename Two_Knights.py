def solve(k):
    all_ways = k**2 * (k**2-1) / 2
    possible_ways = all_ways - (k-1)*(k-2)*4

    return int(possible_ways)

n = int(input())

for i in range(1,n+1):
    print(solve(i))

