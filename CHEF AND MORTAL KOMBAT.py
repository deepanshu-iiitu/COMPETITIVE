t = int(input())
for x in range(0, t):
    n, k = [int(i) for i in input().split()]
    mk = [int(i) for i in input().split()]
    ct = [int(i) for i in input().split()]
    mk.sort()
    ct.sort()
    c = 0
    ans = 0
    for a in range(0, n):
        for b in range(c, n):
            if ct[a] > mk[c]:
                ans += 1
                break