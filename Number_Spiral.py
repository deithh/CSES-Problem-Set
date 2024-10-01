n = int(input())

for i in range(n):
    a, b = [int(x) for x in input().split()]

    steps = min(a, b) - 1
    main_square = max(a, b) ** 2


    if a>b:
        direction = 1 if a%2 == 0 else -1
    else:
        direction = 1 if b%2 == 1 else -1

    if direction == -1:
        steps = main_square - (max(a, b)-1)**2 - steps - 1

    print(main_square-steps)

        