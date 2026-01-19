def mini(L):
    mini =L[0]
    for i in L:
        if i<mini:
            mini = i
    return mini
def sort(L):
    if (L==[]) or (len(L) ==1 ):
        return L
    else:
        m = mini(L)
        L.remove(m)
        return [m]+sort(L) 
    