n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
for i in range(0, k):
    for j in range(1, n):
        a[j] = a[j-1] | a[j]
print(*a)