#https://codeforces.com/contest/2123/problem/F
prime = [True]*(10**5+1)
prime[0] = False
prime[1] = False
p = []
for i in range(2, 317):
    if prime[i]:
        for j in range(i**2, 10**5+1, i):
            prime[j] = False
for i in range(2, 10**5+1):
    if prime[i]:
        p.append(i)
p.reverse()
for _ in range(int(input())):
    n = int(input())
    f = [0]*(n+1)
    for i in p:
        if i>n:
            continue
        c = []
        for j in range(i, n+1, i):
            if not f[j]:
                c.append(j)
        for j in range(len(c)):
            f[c[j]] = c[(j+1)%len(c)]
    for i in range(n+1):
        if not f[i]: f[i] = i
    print(*f[1:], sep = " ")
