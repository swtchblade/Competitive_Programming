#https://codeforces.com/contest/2123/problem/D
for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    c = s.count("1")
    print("Alice"if c <= k or 2*k > n else "Bob")
