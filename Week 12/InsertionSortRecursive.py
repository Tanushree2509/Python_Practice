def Insert(L,v):
    n = len(L)
    if n == 0:
        return ([v])
    if v >= L[-1]:
        return (L+[v])
    else:
        return (Insert(L[:1],v)+L[-1:])
def ISort(L):
    n = len(L)
    if n < 1:
        return (L)
    L = Insert(ISort(L[:-1]), L[-1])
    return (L)