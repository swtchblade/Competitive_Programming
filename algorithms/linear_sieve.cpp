int N;
V<int> lp(N);
V<int> pr;
void sieve(){
    FOR(i,2,N){
        if(!lp[i]){lp[i]=i;pr.pb(i);}
        for(int j=0;i*pr[j]<N;j++){
            lp[i*pr[j]]=pr[j];
            if(pr[j]==lp[i]){break;}}}}
