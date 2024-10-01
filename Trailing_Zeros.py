def calc_trailing_zeroes(n):
    factor5 = 0
    current_pow_five = 5
    while(current_pow_five <= n):
        factor5+= n // current_pow_five
        current_pow_five *=5
    return factor5

n = int(input())
print(calc_trailing_zeroes(n))