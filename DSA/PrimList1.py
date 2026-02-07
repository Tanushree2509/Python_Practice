def primlist(WList):
   infinity = 1 + max([d for u in WList.keys() for (v,d) in WList[u]])
   (visited, distance, TreeEdges) = ({},{},[])
   for v in WList.keys():
      (visited[v], distance[v]) = (False, infinity)
   visited[0] = True
   for (v,d) in WList[0]:
      distance[v] = d
   for i in WList.keys():
      (mindist, nextv) = (infinity, None)
      for u in WList.keys():
         for (v,d) in WList[u]:
            if visited[u] and (not visited[v]) and d < mindist:
               (mindist, nextv,nexte)= (d,v,(u,v))
      if nextv is None:
         break
      visited[nextv] = True
      TreeEdges.append(nexte)
      for (v,d) in WList[nextv]:
         if not visited[v]:
            distance[v] = min(distance[v],d)
   return(TreeEdges)