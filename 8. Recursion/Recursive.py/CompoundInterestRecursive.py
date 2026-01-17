def comp(p,n):
    if n==1:
        return p*(1.1)
    else:
        return comp (p,n-1)*1.1