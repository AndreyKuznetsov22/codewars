def get_neighbourhood(n,a,c,d=1):
    
    def v(a,b):
        t=list(abs(e-f) for e,f in zip(a,c))
        if not (m:=max(t)): b.append(1)
        return 1<=m<=d and (n=='moore' or sum(t)<=d)

    def dfs(a,b,c,d=[]):
        if type(a) is int and v(d,b): c.append(a)
        if type(a) is int: return
        for i,e in enumerate(a): dfs(e,b,c,d+[i])
    
    dfs(a,valid:=[],neighbours:=[])
    return neighbours if valid else []