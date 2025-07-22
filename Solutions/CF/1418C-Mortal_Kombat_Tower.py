#https://codeforces.com/contest/1418/problem/C
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = [[10**6]*(n+1) for _ in range(2)]
    d[1][0]=0
    for i in range(0,n):
        d[0][i+1] = min(d[0][i+1],d[1][i]+a[i])
        d[1][i+1] = min(d[1][i+1], d[0][i])
        if i<n-1:
            d[0][i+2] = min(d[0][i+2], d[1][i]+a[i]+a[i+1])
            d[1][i+2] = min(d[1][i+2], d[0][i])
    print(min(d[0][n], d[1][n]))
