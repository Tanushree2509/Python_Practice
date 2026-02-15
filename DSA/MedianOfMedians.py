def MoM(L):
   if len(L) <= 5:
      L.sort()
      return(L[len(L)//2])
   #construct list of block medians
   M = []
   for i in range (0, len(L), 5):
      X = L[i:i+5]
      X.sort()
      M.append(X[len(X)//2])
   return(MoM(M))