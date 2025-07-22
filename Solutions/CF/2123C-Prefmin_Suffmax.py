#https://codeforces.com/contest/2123/problem/C
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    p = [0]*n
    s  = [0]*n
    m = 10**7
    for i in range(n):
        m = min(m, a[i])
        p[i] = m
    m = -1
    for i in range(n-1, -1, -1):
        m = max(m, a[i])
        s[i] = m
    ans = []
    for i in range(n):
        if a[i] == p[i] or a[i] == s[i]:
            ans.append("1")
        else:
            ans.append("0")
    print("".join(ans))
