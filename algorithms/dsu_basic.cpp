struct DSU {
	V<int> e;void init(int N){e=V<int>(N,-1);}
	int get(int x){return e[x] < 0?x:e[x]=get(e[x]);} 
	bool same(int a,int b){return get(a)==get(b);}
	int size(int x){return -e[get(x)];}
	bool uni(int x, int y){
		x = get(x), y = get(y);if (x == y){return 0;}
		if (e[x] > e[y]){swap(x,y);}
		e[x]+=e[y];e[y]=x;return 1;}};
