def upper(s):
    upper = 0
    for c in s:
        if (c.isupper()):
            upper += 1
    return (upper)
def lower(s):
    lower = 0
    for c in s:
        if (c.islower()):
            lower +=1
    return (lower)
def characters(s):
    chars = 0
    for c in s:
        chars += 1
    return (chars)
def words(s):
    words =1
    for c in s:
        if (c ==' '):
            words += 1
    return(words)

sentence = input ("Enter the sentence: ")
uLetters = upper (sentence)
print (f'\n Total number of upper case characters: {uLetters}')
lLetters = lower (sentence)
print (f'\n Total number of lower case characyers: {lLetters}')
chars = characters(sentence)
print (f'\n Total number of characters: {chars}')
words = words(sentence)
print (f'\nTotal number of words: {words}')