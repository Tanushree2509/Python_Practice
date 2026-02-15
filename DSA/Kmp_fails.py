def kmp_fail(p):
   #initialize
   m = len(p)
   fail = [0 for i in range(m)]
   #update
   j, k = 1, 0
   while j < m:
      if p[j] == p[k]: # k+1 chars match
         fail[j] = k+1
         j, k = j+1, k+1
      elif k > 0: #find shorter prefix
         k = fail[ k-1]
      else:
         j = j+1
   return(fail)