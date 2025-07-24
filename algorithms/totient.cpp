//O(sqrt(n))
int phi(int n) {
    int r=n;
    FOR(p,2,sqrt(n)+1){
        if(n%p==0){
            while(n%p==0){n/=p;}
            r-=r/p;}}
    if (n > 1){r-=r/n;}
    return r;}
//O(n logn logn), computes all phi(i) between 1...n
int N=;
V<int> phi(N);
void allphi(){
    FOR(i,1,N){phi[i]=i;}
    FOR(i,2,N){
        if(phi[i]==i){FORJ(j,i,N,i){phi[j]-=phi[j]/i;}}}}
