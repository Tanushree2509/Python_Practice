def NoDupticate(L):
    for i in range(len(L)):
        for j in range (i+1, len(L)):
            if (L[i]==L[j]):
              return False
    return True  