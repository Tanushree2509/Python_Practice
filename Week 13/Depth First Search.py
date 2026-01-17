(visited, parent) = ({}, {})
def DFSInitGlobal (AMat):
    #Initialization
    (rows, cols) = AMat.shape
    for i in range (rows):
        visited[i] = False
        parent[i] = -1
    return
def DFSGlobal (AMat, v):
    visited[v] = True
    for  k in neighbours(AMat, v ):
        if (not visited[k]):
            parent [k] = v
            DFSGlobal (AMat ,k)
    return

#by list
(visited, parent) = ({}, {})
def DFSInitListGlobal(Alist):
    #Initialization
    for i in AList.keys():
        visited[i] = False
        parent[i] = -1
    return
def DFSListGlobal(AList, v):
    visited[v] = True

    for k in AList[v]:
            if (not visited[k]):
                parent[k] = v
            DFSListGlobal (AList, k)
    return