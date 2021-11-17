#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes
temps = (1,3,46,40)
def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    tempsEnSeconde = 86400 * temps[0] + 3600 * temps[1] + 60 * temps[2] + temps[3]
    return tempsEnSeconde

# print(type(temps))
# print(tempsEnSeconde(temps))



def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    jours = seconde // 86400
    reste = seconde % 86400
    heures = reste // 3600
    reste2 = reste % 3600
    minutes = reste2 // 60
    seconde = reste2 % 60
    secondeEnTemps = jours, heures, minutes, seconde
    return secondeEnTemps

# temps = secondeEnTemps(100000)
# print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")


#fonction auxiliaire ici

def afficheTemps(temps):
    if temps[0] == 1 :
        print(temps[0],"jour" , end=" ")
    elif temps[0] > 1 :
        print(temps[0],"jours", end=" ")

    if temps[1] == 1 :
        print(temps[0],"heure" , end=" ")
    elif temps[1] > 1 :
        print(temps[0],"heures", end=" ")

    if temps[2] == 1 :
        print(temps[2],"minute" , end=" ")
    elif temps[2] > 1 :
        print(temps[2],"minutes", end=" ")
   
    if temps[3] == 1 :
        print(temps[3],"seconde" , end=" ")
    elif temps[3] > 1 :
        print(temps[3],"secondes", end=" ")




afficheTemps((1,0,14,23))

entrejours = 0
entreheures = 0
entreminutes = 0
entresecondes = 0

def demandeTemps():
    while entrejours > 31 or entrejours < 0 :
        int(input("entrez un jour"))
    print(entrejours,"jours", end=" ")
    
    while entreheures > 24 or entreheures < 0 :
        int(input("entrez heures"))
    print(entreheures,"heures",end=" ")

    while entreminutes > 60 or entreminutes < 0 :
        int(input("entrez minutes"))
    print(entreheures,"minutes",end=" ")
    
    while entresecondes > 60 or entresecondes < 0 :
        int(input("entrez secondes"))
    print(entreheures,"secondes",end=" ")

afficheTemps(demandeTemps())