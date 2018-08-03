from decimal import Decimal
t = int(input())
for t in range(0,t):
    x,n,d,k = [x for x in input().split()]
    x = int(x)
    n = int(n)
    p = 1
    for n in range(0,n-1):
        p = p * (x-1) / x
        x -=1
    p = p / x
    x = Decimal(p)
    output = round(x, 10)
    print(output)