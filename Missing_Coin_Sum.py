def solve(arr):

    arr.sort()
    expected = 1

    for i in arr:
        #if i<= expected we can use i and previous checked values to generate any value to i+expected-1
        if i > expected:
            return expected 
        
        expected += i
        
    return expected 


def main():
    n = int(input())
    arr  = [int(x) for x in input().split()]

    print(solve(arr))


if __name__ == "__main__":
    main()