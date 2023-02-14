def fonction(s):
    l=[]
    for i in s:
        for e in l:
            if e[0]== i:
                e[1]+=1
                break
        l.append([i,1])