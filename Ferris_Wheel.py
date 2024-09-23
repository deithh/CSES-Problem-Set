n, x = [int(x) for x in input().split()]
 
pi = [int(x) for x in input().split()]
 
pi.sort()
 
 
count = 0
i, j = 0, len(pi) - 1
 
while i<j:
 
    i += (pi[i] + pi[j] <= x)
    j-=1
    count += 1
 
if i==j:
    count+=1
 
 
print(count)