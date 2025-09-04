def string_times(s,n): return s*n #$
def front_times(s,n):return s[:3]*n #$
def string_bits(s):return s[::2] #$
def string_splosion(s):return s and string_splosion(s[:-1])+s #$
def last2(s):return [*zip(s,s[1:-1])].count((*s[-2:],)) #$
def array_count9(n):return n.count(9) #$
def array_front9(n):return 9 in n[:4] #$
def array123(n):return(1,2,3)in zip([0]+n,n,n[1:]) #1 off
def string_match(a,b):return sum(x==x[::-1] for x in zip(a,a[1:],b[1:],b)) #4 off
#logic2
def make_bricks(s,b,g):return g%5<=s>=g-b*5 #$
def lone_sum(a,b,c):return sum({a,b,c})*2-a-b-c+c*(a==b==c) #1 off
def lucky_sum(a,b,c):return (a!=13)*(a+(b!=13)*(b+(c!=13)*c)) #1 off
def no_teen_sum(a,b,c):return sum(x-x*(12<x<15 or 16<x<20) for x in [a,b,c]) #4 off
def round_sum(a,b,c):return sum((x+5)//10for x in(a,b,c))*10 #$
def close_far(a,b,c):return abs(b-c)>1and(-2<a-b<2)^(-2<a-c<2) #1 off
def make_chocolate(s,b,g):return [e:=max(g-5*b,g%5),-1][s<e]#$
#string2
def double_char(s): return "".join(i*2 for i in s) #$
def count_hi(s):return s.count("hi") #$
def cat_dog(s):return (c:=s.count)('cat')==c('dog') #$
def count_code(s):return [*zip(s,s[1:],s[3:])].count((*"coe",)) #~3 off
def end_other(a,b):return b.lower()[-len(a):]==a.lower()[-len(b):] #$
def xyz_there(s):return "xyz"in s.replace(".x"," ") #$
#list2
def count_evens(n):return sum(~i%2 for i in n) #$
def big_diff(n):return max(n)-min(n)#$
def centered_average(n):return sum(n:=sorted(n)[1:-1])//len(n) #$
def sum13(n):return [f:=1]and sum(f*(f:=x!=13)*x for x in n) #~4 off
def sum67(n):return [f:=1]and sum(f*(f:=x!=6and(x==7or f))*x for x in n) #~12 off
def has22(n):return(2,2)in zip([0]+n,n) #$
#Nathan, Period 5, 2027