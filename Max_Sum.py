t = int(input())
for t in range(0, t):
    x, k = [int(x) for x in input().split()]
    ans = 0
    if k ==0:
        ans = 0
    elif x%k == 0:
        ans = (x//k) ** k
    elif x%k != 0:
        ans = (((x//k)+1) ** (k-1))*(x - (((x//k)+1) ** (k-1)))
    print(ans % 10000007)