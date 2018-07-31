n, m = [int(x) for x in input().split()]
if n > m:
    c = n
    n = m
    m = c
lcm = 0
j = n*m
for i in range(j, m, -1):
    if i%n == 0 and i%m == 0:
        lcm = i
print(lcm)