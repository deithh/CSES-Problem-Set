seq = input()
seq = seq + 'EOF'
last = None
maxsize = 1
size = 1
 
 
for i in seq:
    if i == last:
        size += 1
    else:
        if size>maxsize:
            maxsize=size
        size=1
    last = i
 
print(maxsize)