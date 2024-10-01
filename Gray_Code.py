
def gen_gray(n):
    if n==1:
        return ['0','1']
    
    last = gen_gray(n-1)

    current_code = ['0' + i for i in last]
    last.reverse()
    current_code += ['1' + i for i in last]

    return current_code

print("\n".join((gen_gray(int(input())))))