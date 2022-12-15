#https://www.codewars.com/kata/5ff0fc329e7d0f0010004c03

def count_diamonds(a,q):
    n=len(a);m=len(a[0])
    if q==0: return [ [[i,j],[i,j]] for i in range(n) for j in range(m) if a[i][j]==0 ]
    ans = []
    size = n*m
    for u in range(n):
        s=[0]*(m)
        for d in range(u,n):
            l=0;cur=0
            for r in range(m):
                s[r]+=a[d][r]
                cur+=s[r]
                while cur-s[l]>=q:
                    cur-=s[l];l+=1
                if cur==q:
                    sz=(d-u+1)*(r-l+1)
                    res=[(u,l),(d,r)]
                    if sz<size: size=sz;ans=[res]
                    elif sz==size: ans.append(res)
    return sorted(ans)