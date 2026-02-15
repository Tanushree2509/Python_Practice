def find_kmp(t, p):
   n, m = len(t), len(p)
   if m ==0:
      return 0 #pattern is empty
   fail = kmp_fail; (p) #preprocessing
   j = 0 #indec into text
   k = 0 #index into pattern
   while j < n :
      if t[j] == p[k]: #matched p [0: k+1]
         if k == m - 1: #match is compllete
            return (j-m+1)
         j, k = j+1, k+1 #extend match
      elif k > 0:
         k = fail[k-1] #use smaller prefix
      else:
         j = j+1
   return (-1) #reached end without match
