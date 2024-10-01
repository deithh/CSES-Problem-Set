import cProfile
def main():
    l, _ = [int(x) for x in input().split()]
    seq = [int(x) for x in input().split()]

    res = [l]

    for i in seq:
        current_sum = i
        for ind, j in enumerate(res):
            if i>j:
                i -= j
            else:
                del res[ind]
                res.insert(ind, j-i)
                res.insert(ind, i)
                break

        print(max(res))

cProfile.run("main()")