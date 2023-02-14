def fonction(s):
    l=[]
    elem =[]
    for i in s:
        if i in elem:
            for e in l:
                if e[0]== i:
                    e[1]+=1
        else:
            l.append([i,1])
            elem.append(i)
    return l
print(fonction("aabcda"))