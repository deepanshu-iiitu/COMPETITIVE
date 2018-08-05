import math
t = int(input())
for t in range(0, t):
    n = int(input())
    i = int(math.log(n, 2))
    li = []
    if n == 1:
        print(2)
        li = li.append(2)
        continue
    for i in range(0, i+1):
        for j in range(0, i+1):
            if i != j:
                k = abs(n - ((2 ** i) + (2 ** j)))
                li = li.append(k)
    sorted(li)
    b = list(set(li))
