import math
 
n = int(input())
count = 0
 
 
 
while n>0:
    base = math.floor(math.log2(n))
    if(base>0):
        count += 2**(base-1)*base + 1
    else:
        count += 1
    n -= 2 ** base
    n >> 1
    count += n
 
print(int(count))