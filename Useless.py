t = int(input())
for t in range(0,t):
    a,b = [int (x) for x in input().split()]
    ans = 0
    for i in range(a,b):
        for j in range(i+1,b+1):
            k = a & b
            if k > ans:
                ans = k
    print(ans)