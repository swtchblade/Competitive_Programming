struct DSU {
	vi e;int c;
	DSU(int n):e(n,-1),c(n){}
	int get(int x){int r=x;while(e[r]>=0){r=e[r];}
    	while(x!=r){int p=e[x];e[x]=r;x=p;}return r;}
	bool same(int a,int b){return get(a)==get(b);}
	int sz(int x){return -e[get(x)];}
	bool uni(int x,int y){
		x=get(x),y=get(y);if(x==y){return 0;}
		if(e[x]>e[y]){swap(x,y);}
		e[x]+=e[y];e[y]=x;c--;return 1;}};
