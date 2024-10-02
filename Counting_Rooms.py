import sys
import cProfile
import threading

threading.stack_size(67108864) 
sys.setrecursionlimit(1000)

def seek(x, y, data, n, m):
    stack = [(x, y)]

    while len(stack) > 0:
        x, y  = stack.pop()
        if x+1<n and data[x+1][y]=='.':
            stack.append((x+1, y))
            data[x+1][y] = 'o'
        if x-1>=0 and data[x-1][y]=='.':
            stack.append((x-1, y))
            data[x-1][y] = 'o'
        if y+1<m and data[x][y+1]=='.':
            stack.append((x, y+1))
            data[x][y+1] = 'o'
        if y-1>=0 and data[x][y-1]=='.':
            stack.append((x, y-1))
            data[x][y-1] = 'o'

def main():
    count = 0

    data = [line.rstrip() for line in sys.stdin.readlines()]
    n, m = [int(x) for x in data[0].split()]
    building = [list(x) for x in data[1:]]


    for i in range(0, n):
        for j in range(0,m):
            if building[i][j] == '.':
                count +=1
                seek(i, j, building, n, m)



    print(count)

main()