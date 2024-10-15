def solve(arr):
    arr.sort()
    median = arr[len(arr)//2]

    res = 0

    for i in arr:
        res+= abs(i - median)

    return res


def main():
    n = int(input())
    arr  = [int(x) for x in input().split()]

    print(solve(arr))


if __name__ == "__main__":
    main()