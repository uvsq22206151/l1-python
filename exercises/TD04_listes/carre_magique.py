print("Question3")
def affiche(carre):
    """ Affiche la liste à 2 dimensions carre comme une ligne """
    print(carre)

carre_mag=[ [4,14,15,1] , [9,7,6,12] , [5,11,10,8] , [16,2,3,13] ]

carre_pas_mag=[ligne[:] for ligne in carre_mag]
carre_pas_mag[3][2]=7
affiche(carre_mag)
affiche(carre_pas_mag)   
print(" ")   

print("Question4")
#Q4 
def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré """
    for ligne_carre in carre:             # la mm chose que i range len(carre)
        print(ligne_carre)
afficheCarre(carre_mag)     
print()  
afficheCarre(carre_pas_mag)
print(" ")

print("Question5")
#Q5
def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si toutes les lignes ont la même somme, et -1 sinon """

    somme= sum(carre[0])

    for somme_ligne in carre:
        if somme != sum(somme_ligne):
            return -1
    return somme 

print(testLignesEgales(carre_mag))
print(testLignesEgales(carre_pas_mag))    

print(" ")
print("Question6")
#Q6
def testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre si toutes les colonnes ont la même somme, et -1 sinon """
    c1=[ligne[0]for ligne in carre]
    somme1= sum(c1)
    for nombre_colone in range(1,len(carre)):
        c2=[ligne[nombre_colone] for ligne in carre]
        if somme1 != sum(c2):
            return -1
    return somme1    

print(testColonnesEgales(carre_mag))
print(testColonnesEgales(carre_pas_mag))    

print(" ")
print("Question7")
def testDiagonalesEgales(carre):
    """ Renvoie la somme des éléments d'une diagonale de la liste 2D carre si les 2 diagonales ont la même somme, et -1 sinon """
    diagonal1=[carre[i][i]for i in range(len(carre))]
    diagonal2=[carre[i][len(carre)-i-1] for i in range(len(carre))]
    somme1=sum(diagonal1)
    if somme1 != sum(diagonal2):
        return -1
    return somme1

print(testDiagonalesEgales(carre_mag))
print(testDiagonalesEgales(carre_pas_mag))


print(" ")
print("Question8")
def estCarreMagique(carre):
    """ Renvoie True si c'est un carre magique et False sinon"""
    return testDiagonalesEgales(carre)== testLignesEgales(carre) == testColonnesEgales(carre) == testDiagonalesEgales(carre) and testLignesEgales !=-1
    
print(estCarreMagique(carre_mag))
print(estCarreMagique(carre_pas_mag))

print(" ")
print("Question9")
def estNormal(carre):
    """ Retourne True si contient toutes les valeurs de 1 à n^2 où n est la taille 
        du carré, et False sinon """
    liste=[]
    for ligne in carre:
        liste.extend(ligne)
    for i in range(1,len(carre)*len(carre)+1):
        if i not in liste: 
            return False
    return True           

print(estNormal(carre_mag))
print(estNormal(carre_pas_mag))