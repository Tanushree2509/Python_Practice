# Dictionaries
malgudi= ['My', 'Reflection', 'by', 'Night','by', 'Du', 'Fu',
        'Some','scattered', 'grass', 'A', 'shore', 'breeze', 'blowing', 'light',
        'A', 'giddy', 'mast', 'A', 'lonely', 'boat', 'at', 'night.',
        'The', 'wide-flung', 'stars', "o'erhang", 'all', 'vasty', 'space',
        'The', 'moonbeams', 'with', 'the', "Yangtze's", 'current', 'race.',
        'How', 'by', 'my', 'pen', 'can', 'I', 'to', 'fame', 'attain',
        'Worn', 'out', 'from', 'office', 'better', 'to', 'refrain',
        'Drifting', "o'er", 'life', 'and', 'what', 'in', 'sooth', 'am', 'I',
        'A', 'sea-gull', 'floating', 'twixt', 'the', 'Earth', 'and', 'Sky']
print (malgudi)
s= set(malgudi)
print(s)
#Length of the list malgudi and the set s
len_malgudi= len(malgudi)
len_s= len(s)
print(len_malgudi)
print(len_s)
d={} #Creating an empty dictionary
#Assigning 0 as the initial frequency of each word in the set s
for x in s:
    d[x]=0
print(d)
#Prints the frequency of each word in the list malgudi
for x in malgudi:
    d[x]= d[x]+1
print(d)

#Find the maximum frequency among all words in the list malgudi
max= 0
d={}
for x in s:
    d[x]=0
for x in malgudi:
    d[x]= d[x]+1
    if d[x]>max:
        max=d[x]   
        word=x
print("Word with maximum frequency is:", word)
print("Maximum frequency is:", max)
