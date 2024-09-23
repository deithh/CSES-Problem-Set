n = int(input())
print(n, end='')
 
 
while n!=1:
	if n%2 == 0:
		n = n>>1
	else:
		n = n * 3 + 1
 
	print(f" {n}", end = '')