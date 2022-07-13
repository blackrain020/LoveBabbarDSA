def reverseWord(s):
    
    reverse=""
    i = len(s)-1

    while i >=0:
        reverse = reverse+(s[i])
        i=i-1
    return reverse
