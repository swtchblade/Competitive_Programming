#https://codeforces.com/contest/2123/problem/E
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = [0]*(n+1)
    for x in a:
        c[x]+=1
    p = [False]*(n+1)
    p[0] = True
    for m in range(1, n+1):
        p[m] = p[m-1] and (c[m-1]>0)
    d = [0]*(n+2)
    for m in range(0, n+1):
        if not p[m]:
            continue
        l = c[m]
        h = n-m
        if l<=h:
            d[l]+=1
            d[h+1]-=1
    a = [0]*(n+1)
    s = 0
    for k in range(0, n+1):
        s += d[k]
        a[k] = s
    print(*a)
