MOD = 10**9 +7
res = [1]
for i in range(int(input())):
    res.append(sum(res[-6:]))
    res[-1] %= MOD
print(res[-1])