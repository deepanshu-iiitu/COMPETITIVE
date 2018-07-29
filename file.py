t = int(input())
for t in range(t):
    n = int(input())
    x=0
    ans =0
    for n in range(n):
        x= x+ 9*(10**n)
    for x in range(x):
        z = x
        y=0
        for j in range(n,0,-1):
            if x >0:
                y = y + (x%10)
                x = x//10
        if y == z:
            ans += 1
    print(ans)