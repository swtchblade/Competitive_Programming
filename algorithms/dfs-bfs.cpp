V<bool> v;
V<V<int>> ad;
void dfs(int i){
    v[i] = true;
    each(a, ad[i]){if(!v[a]){dfs(a);}}}
void bfs(int i){
    deque<int> q;q.pb(i);v[i] = true;
    while(!q.empty()){int c = q.ft;q.pof();
        each(a, ad[c]){if(!v[a]){v[a]=true;q.pb(a);}}}}
