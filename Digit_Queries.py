n = int(input())

def querry(n):
    lvl = 9
    i = 1
    while n > lvl:
        n -= lvl
        lvl = 10**i * 9 * (i+1)
        i+=1
    
    ind = (n) //(i)
    pos = n%i
    if pos == 0:
        ind -= 1
        pos = i-1
    else:
        pos -=1
    res = ind + 10**(i-1)

    return str(res)[pos]


for i in range(n):
    print(querry(int(input())))