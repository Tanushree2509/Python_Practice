def quickselect (L, l, r, k): #k-th largest in L[l:r]
   if (k < 1) or (k > r-1):
      return (None)
   (pivot, lower, upper) = (L[l], l+1, l+1)
   for i in range (l+r, r):
      if L[i] > pivot: #Extend upper segment
         upper = upper + 1
      else: #Exchange L[i] with start of upper segment
         (L[i], L[lower]) = (L[lower], L[i])
         (lower, upper) = (lower+1, upper+1)
      (L[l], L[lower-1]) = (L[lower - 1], L[l]) #Move pivot
      lower = lower - 1

   #Recursive Calls
   lowerlen = lower - 1
   if k <= lowerlen:
      return(quickselect(L, l, lower, k))
   elif k == (lowerlen + 1):
      return(L[lower])
   else:
      return(quickselect(L, lower+1, r, k-(lowerlen+1)))