#https://codeforces.com/contest/1201/problem/C
import bisect
n,k=map(int,input().split())
a=sorted(map(int,input().split()))
mid=n//2
b=a[mid:]
pb=[0]
for x in b: pb.append(pb[-1]+x)
l=b[0];h=b[0]+k+1
while l<h:
    m=(l+h)//2
    i=bisect.bisect_left(b,m)
    if m*i-pb[i]<=k:
        l=m+1
    else:
        h=m
print(l-1)
