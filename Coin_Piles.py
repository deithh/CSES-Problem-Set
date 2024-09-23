n = int(input())
 
def check(c, d):
 
    a = (2*c - d)/3 
    b = (2*d - c)/3
 
    if(a<0 or b<0):
        return False
    if (a == int(a) and b == int(b)):
        return True
    return False
 
 
for i in range(n):
 
    a, b = [int(x) for x in input().split()]
    if check(a, b):
        print("YES")
    else:
        print("NO")