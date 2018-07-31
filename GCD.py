n, m = [int(x) for x in input().split()]
gcd = 1
if n>m:
    c = n
    n = m
    m = c
for i in range(2,n+1):
    if n%i == 0 and m%i ==0:
        gcd = i
print(gcd)