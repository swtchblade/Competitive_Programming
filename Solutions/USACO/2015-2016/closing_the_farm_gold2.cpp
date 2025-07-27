#include <bits/stdc++.h>
using namespace std;
#define tcT template<class T
tcT> using V=vector<T>;tcT> using S=set<T>;tcT> using Q=deque<T>;
using ll=long long;using ld=long double;using db=double;using str=string;
using pi=pair<int,int>;using pl=pair<ll,ll>;
using vi=V<int>;using vl=V<ll>;using vb=V<bool>;using vs=V<str>;using vpi=V<pi>;
#define len(a) a.size()
#define rz resize
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define FORJ(i,a,b,c) for(int i=a;i<b;i+=c)
#define ROF(i,b,a) for(int i=b;i>a;i--)
#define ROFJ(i,b,a,c) for(int i=b;i>a;i-=c)
#define each(a,x) for (auto& a:x)
#define all(x) begin(x),end(x)
#define rall(x) rbegin(x),rend(x)
#define so(x) sort(all(x))
#define sor(x) sort(rall(x))
#define pb push_back
#define pf push_front
#define pob pop_back
#define pof pop_front
#define ft front()
#define bk back()
#define mp make_pair
#define f first
#define s second
struct DSU {
	vi e;int c;
	DSU(int n):e(n,-1),c(n){}
	void inc(){e.pb(-1);c++;}
	int get(int x){int r=x;while(e[r]>=0){r=e[r];}
    	while(x!=r){int p=e[x];e[x]=r;x=p;}return r;}
	bool same(int a,int b){return get(a)==get(b);}
	int sz(int x){return -e[get(x)];}
	bool uni(int x,int y){
		x=get(x),y=get(y);if(x==y){return 0;}
		if(e[x]>e[y]){swap(x,y);}
		e[x]+=e[y];e[y]=x;c--;return 1;}};
int main() { 
	ios::sync_with_stdio(0);
	cin.tie(0);
	freopen("closing.in","r",stdin);freopen("closing.out","w",stdout);
	int n,m;cin>>n>>m;
	vpi r;int x,y;
	FOR(i,0,m){cin>>x>>y;x--;y--;r.pb(mp(x,y));}
	vi o(n); map<int,int> ind;
	ROF(i,n-1,-1){cin>>x;x--;ind[x]=i;o[i]=x;}
	V<vi> ed(n);
    each(a,r){
        int iu=ind[a.f], iv=ind[a.s];
        if(iu<iv){ed[iv].pb(iu);} else{ed[iu].pb(iv);}}
    DSU d(1);
	vs a;a.pb("YES");
	FOR(i,1,n){
	    d.inc();
	    each(j,ed[i]){d.uni(i,j);}
	    a.pb(d.c==1?"YES":"NO");
	}
	reverse(all(a));
	each(s,a){cout<<s<<"\n";}
}
