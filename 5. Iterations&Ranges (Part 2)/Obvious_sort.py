#find out the minimum most number in a list l
#append that to a new list x
#remove that minimum number from the original list l
#repeat until l is empty
#Type 1
def min_list(l):
    min_num= l[0]
    for i in range(len(l)):
        if l[i]<min_num:
            min_num = l[i]  
    return min_num
def obvious_sort(l):
    x=[]
    while(len(l)>0):
        min_num= min_list(l)
        x.append(min_num)
        l.remove(min_num)
    return x
'''

#Type 2
def obvious_sort(l):
    x=[]
    while(len(l)>0):
        min_num= l[0]
        for i in range(len(l)):
            if l[i]<min_num:
                min_num = l[i]  
        x.append(min_num)
        l.remove(min_num)
    return x
'''
l=[5,3,8,6,2,7,4,1]
print(obvious_sort(l))