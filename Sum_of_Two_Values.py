def bin_search(arr, x, exclude) -> int:
 
    begin, end = 0, len(arr)-1
 
    while begin<=end:
        mid = (begin + end)//2
        if arr[mid][1] == x:
            if mid != exclude:
                return mid
            if mid > 0 and arr[mid-1][1] == x:
                return mid-1
            if mid < len(arr)-1 and arr[mid+1][1]==x:
                return mid+1
            return -1
        elif arr[mid][1] < x:
            begin =mid + 1
        else:
            end = mid - 1
    
    return -1
 
def solve(arr, val) -> str:
    arr.sort(key = lambda x: x[1])
 
    for ind, i in enumerate(arr):
        if i[1] > val:
            return "IMPOSSIBLE"
        
        found_ind = bin_search(arr, val - i[1], ind)
        if found_ind >= 0:
            return f"{i[0]+1} {arr[found_ind][0]+1}"
    return "IMPOSSIBLE"
 
 
def main() -> None:
    n, val = [int(x) for x in input().split()]
    arr  = [(ind, int(x)) for ind, x in enumerate(input().split())]
 
    print(solve(arr, val))
 
 
if __name__ == "__main__":
    main()