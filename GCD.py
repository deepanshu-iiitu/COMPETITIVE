t = int(input())
for t in range(0,t):
    a, b, n = [int(x) for x in input().split()]
    gcd = 1
    u = (a**n) + (b**n)
    d = a-b
    if d == 0:
        print(u)
        continue
    for i in range(2, d+1):
        if u % i == 0 and d % i == 0 and d != 0:
            gcd = i
    print(gcd % 1000000007)