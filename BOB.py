t = int(input())
for x in range(0,t):
    a = input()
    b = input()
    v = {a[0]+a[1]+a[2], a[0]+b[1]+a[2], a[0]+a[1]+b[2], a[0]+b[1]+b[2], b[0]+a[1]+a[2], b[0]+b[1]+a[2], b[0]+a[1]+b[2],
         b[0]+b[1]+b[2]}
    if 'bob' in v or 'obb' in v or 'bbo' in v:
        print("yes")
    else:
        print("no")