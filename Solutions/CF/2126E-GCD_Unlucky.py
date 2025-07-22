#https://codeforces.com/contest/2126/problem/E
from math import gcd
def solve():
    n = int(input())
    p = list(map(int, input().split()))
    s = list(map(int, input().split()))
    if p[-1]!=s[0]:return "NO"
    for i in range(1, n):
        if p[i-1]%p[i] or p[i]%gcd(p[i-1], s[i]):
            return "NO"
    for i in range(n-1):
        if s[i+1] % s[i] or s[i]%gcd(p[i],s[i+1]):
            return "NO"
    return "YES"
for _ in range(int(input())):
    print(solve())
