#https://codeforces.com/contest/2118/problem/C
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(lambda x: (bin(int(x))[2:]).zfill(60)[::-1], input().split()))
    r = 1
    i = 0
    s = sum(x.count('1') for x in a)
    while k>=r:
        for x in a:
            if x[i] == '0' and k>=r:
                s+=1
                k-=r
        r *= 2
        i += 1
    print(s)
