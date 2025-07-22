for _ in range(int(input())):
    n,k=map(int,input().split())
    k-=1
    a = list(map(int,input().split()))
    b = a.copy()
    b.sort()
    h=1
    pos = a[k]
    i = b.index(a[k])
    t = b[-1]
    while b[i]!=t:
        if b[i+1]-b[i]<=b[i]-h+1:
            h+=b[i+1]-b[i];i+=1
        else:
            break
    print("YES" if b[i]==t else "NO")
