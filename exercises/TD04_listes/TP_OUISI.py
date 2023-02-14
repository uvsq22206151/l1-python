G=[[0,0,0],[0,0,0],[0,0,0]]


#Les différentes fonctions
def affiche(carre):
    for i in carre:
        print(i)

def valide(gr,ll,cc):
    if G[l][c] ==0:
        valide == True
    else:
        valide == False 


def FinJeu(GG,joueur):
    v=[joueur,joueur,joueur]
    # Par ligne
    if v in GG:
        return True
    else: 
        n=len(GG)
        for j in range(n):
            l=[]
            for i in range(n):
                l.append(GG[i][j])
            if v==l:
                return True
            # premiere diag
            l.clear()
            l=[]
            for i in range(n):
                l.append(GG[i][i])
            if v==l:
                return True
            # deuxièle diag
            l.clear()
            l=[]
            for i in range(n):
                l.append(GG[i][n-i-1])
            if v==l:
                return True

    return False
        
        
affiche(G) 

joueur=1
gagnant=False


while gagnant==False:
    if joueur==1:
        l=int(input("choisir une ligne"))
        c=int(input("choisir une colone"))
        while(valide(G,l,c)==False):
            l=int(input("choisir une autre ligne"))
            c=int(input("choisir une autre colone"))
        G[l][c]=1
        affiche(G)
        gagnant=FinJeu(G,1)
        if gagnant==False:
            joueur=2
    else:
        l=int(input("choisir une ligne"))
        c=int(input("choisir une colone"))
        while(valide(G,l,c)==False):
            l=int(input("choisir une autre ligne"))
            c=int(input("choisir une autre colone"))
        G[l][c]=2
        affiche(G)
        gagnant=FinJeu(G,2)
        if gagnant==False:
            joueur=1

