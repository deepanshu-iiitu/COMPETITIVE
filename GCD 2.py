t = int(input())
for t in range(0, t):
    a, b, n = [int(x) for x in input().split()]
    gcd = 1
    u = (a**n) + (b**n)
    v = a-b
    while v > 0:
        if u == v:              #v=0 case missing
            gcd = u
            continue
        if u%2 == 0:
            if v%2 == 0:
                