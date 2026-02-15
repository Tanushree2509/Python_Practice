def fastselect(L, l, r, k): #K-th largest in L[l:r]
   if (k < 1) or (k > r-1):
      return (None)
   #Find MoM pivot and move to L[l]
   pivot = MoM(L[l:r])
   pivotpos = min(i for i in range (l,r) if L[i] == pivot)
   (L[l], L[pivotpos]) = (L[pivotpos, L[l]])
   #Partition as before
   (pivot, lower, upper) = (L[l], l+1, l+1)
   for i in range (l+1, r):



   # Recursive Calls
   lowerlen = lower - 1
   if k <= lowerlen:
      return (fastselect(L, l, lower, k))
   elif k == (lowerlen + 1):
      return(L[lower])
   else:
      return(fastselect(L, lower+1, r, k- (lowerlen+1)))
   