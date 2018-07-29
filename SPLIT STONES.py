t = int(input())
for i in range(0, t):
    a, b, c, x, y = [int(x) for x in input().split()]
    mi = a
    if mi > b:
        mi = b
    if mi > c:
        mi = c
    if a+b+c == x+y and mi <=x and mi<=y:
        print('YES')
    else:
        print('NO')