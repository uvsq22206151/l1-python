def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    liste=[n]
    while n!=1:
        if n%2==0:
            n=n//2
        else:
            n=n*3+1    
        liste.append(n)
    return liste        

print(syracuse(3))



#
def testconjoncture(n_max):
    for i in range(1,n_max+1):
        syracuse(i)
    return True 


#
def tempsVol(n):
    return(len(syracuse(n))-1)

#
def tempsVolListe(n_max):
    return[tempsVolListe(i)for i in range(1,n_max+1)]
liste_temps=tempsVolListe(10000)
temps_max=max(liste_tamps)
    print("l'entier", liste_temps.index(temps_max)+1 "a le plus grand temps de vol a", temps_max) 

# la meme chose les 2exo donc regarder si pb

#
def alt_max(n):
    return(max(syracuse(n))) 
def alt_max_liste(n_max):
    return[alt_max(i) for i in range(1, n_max+1)]   
liste_alt=alt_max_liste(10000)
altitude_max=max(liste_alt)
print("l'entier",liste_alt.index(altitude_max)+1," a la plus grande altitude max a",altitude_max)             