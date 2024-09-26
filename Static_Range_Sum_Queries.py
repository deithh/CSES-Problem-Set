import math
def seek_tree(tree, h, a, b):
    if a>b:
        return 0
    
    pa, pb = (1<<h) + a, (1<<h)+b
    res = tree[pa]
    if pa!=pb:
        res += tree[pb]

    while (pa//2 != pb//2):

        if pa%2 == 0:
            res += tree[pa+1]
        if pb%2 == 1:
            res += tree[pb-1]
        
        pa //= 2
        pb //= 2

    return res

def set_tree(tree, h, pos, x):
    target = (1<<h) + pos

    tree[target] = x

    while target > 1:
        target //= 2
        tree[target] = tree[target * 2] + tree[target * 2 + 1]


def construct_tree(seq):
    h = math.ceil(math.log2(len(seq)))
    nodes = 1<<(1+h)

    tree = [0]*nodes

    for ind, i in enumerate(seq):
        set_tree(tree, h, ind, i)

    return tree, h

n = int(input().split()[1])
seq = [int(x) for x in input().split()]
tree, h = construct_tree(seq)

for i in range(n):
    a, b = [int(x) - 1 for x in input().split()]
    print(seek_tree(tree, h, a, b))