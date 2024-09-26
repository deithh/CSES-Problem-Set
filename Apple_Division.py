def solve(ind, array, currL, currR):

    if ind == len(array):
        return abs(currL - currR)
    
    r = solve(ind + 1, array, currL, currR + array[ind])
    l = solve(ind + 1, array, currL + array[ind], currR)

    return min(r, l)


n = int(input())
pis = [int(x) for x in input().split()]


print(solve(0, pis, 0, 0))