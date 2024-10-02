def perm(arr):
    result = []
    arr.sort()
  
    while True:
        result.append(arr.copy())
        
        k = -1
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                k = i
                
        if k == -1:
            break
        
        l = -1
        for i in range(k + 1, len(arr)):
            if arr[k] < arr[i]:
                l = i
        
        arr[k], arr[l] = arr[l], arr[k]
        
        arr = arr[:k + 1] + arr[k + 1:][::-1]
    
    return result

def main():
    word = list(input())
    result = perm(word)
    result = ["".join(x) for x in result]
    result = set(result)
    print(len(result))
    result = list(result)
    result.sort()
    print("\n".join(result))
main()


