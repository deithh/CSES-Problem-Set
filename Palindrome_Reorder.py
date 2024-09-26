from collections import Counter

def pal_from_counter(C: Counter):
    char, mul = '', 0
    temp = []
    for i, times in C.items():
        if times%2 == 1:
            char, mul = i, times
            continue
        times //= 2
        for k in range(times):
            temp.append(i)
    string = "".join(temp)
    pal = string + char * mul + string[::-1]
    return pal


letters = input() 

C = Counter(letters)
check = [1 for n in C.values() if n%2 ==1]

string = ''

if len (check)>1:
    string = "NO SOLUTION"
else:
    string = pal_from_counter(C)


print(string)
