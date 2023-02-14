#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    a = temps[0]*24*3600 + temps[1]*3600 + temps[2]*60 + temps[3]
    return a

temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))   