def rbinarysearch(L,k,begin,end):
    if (begin==end):
        if (L[begin]==k):
            return 1
        else: 
            return 0
    if (end - begin ==1):
        if (L[begin]==k) or (L[end]==k):
            return 1
        else:
            return 0
    if (end - begin >1):
        mid = (begin+end)//2
        if (L[mid]>k):
            end - mid -1
        if (L[mid]<k):
            begin = mid +1
        if (L[mid]==k):
            return 1
    if (end-begin<0):
        return 0
    return rbinarysearch(L,k,begin,end)
