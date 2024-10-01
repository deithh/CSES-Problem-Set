def move(disk, moves, source, target, aux):
    if disk == 1:
        moves.append([source, target])
        return
    
    move(disk - 1, moves, source, aux, target)
    moves.append([source, target])
    move(disk - 1, moves, aux, target, source)


n = int(input())
print(2**n-1)

moves = []
move(n, moves, 1,3,2)
for i in moves:
    print(" ".join(map(str, i)))

