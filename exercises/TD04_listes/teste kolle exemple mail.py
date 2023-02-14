
l=[3,4 , 34 , 53 , 6 , 41 ,15]

def nomdelafonction(n, liste):
    nbdenb=0
    for i in range(len(liste)):
        if liste[i]>n:
            nbdenb+=1
            print("bonjour")
    return nbdenb
print(nomdelafonction(4,l))