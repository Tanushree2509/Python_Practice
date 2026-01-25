def C(dim):
   # dim: dimension matrix
   # entries are pairs (r_i, c_1)
   import numpy as np
   n = dim.shape[0]
   C = np.zeros((n,n))
   for i in range (n):
      C[i,i] = 0 
   for diff in range (i, n):
      for i in range (0, n-diff):
         j = i + diff
         C[i,j] = C[i,i] + C[i+1, j] + dim[i+1][0] + dim[j][i]
         for k in range (i+1, j+1):
            C[i,j] = min ( C[i,j],  C[i, k-1] + C[k,j] + dim[i][0]*dim[j][1])
   return (C[0, n-1])