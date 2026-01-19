def matrixMultiply(A,B):
     (m,n,p) = (len(A), len(B), len(B[0]))
     C =  [ [0 for i in range (p)] for j in range (m)]
     for i in range (m):
          for j in range (p):
               for k in range (n):
                    C[i][j] = C[i][j] + A [i][k]* B[k][j]
     return (C)