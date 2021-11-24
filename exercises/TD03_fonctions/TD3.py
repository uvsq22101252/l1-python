#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes
temps = (1,3,46,40)
def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    tempsEnSeconde = 86400 * temps[0] + 3600 * temps[1] + 60 * temps[2] + temps[3]
    return tempsEnSeconde

print(type(temps))
print(tempsEnSeconde(temps))



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

temps = secondeEnTemps(1000000000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")


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





def demandeTemps():
    entrejours = 0
    entrejours = int(input("entrez un jour"))
    while entrejours > 365 or entrejours < 0 :
        entrejours = int(input("entrez un jour"))
    entreheures = 0
    entreheures = int(input("entrez heures"))
    while entreheures > 24 or entreheures < 0 :
        entreheures = int(input("entrez heures"))
    entreminutes = 0
    entreminutes = int(input("entrez minutes"))
    while entreminutes > 60 or entreminutes < 0 :
        entreminutes = int(input("entrez minutes"))
    entresecondes = 0
    entresecondes = int(input("entrez secondes"))
    while entresecondes > 60 or entresecondes < 0 :
        entresecondes = int(input("entrez secondes"))
    return(entrejours, entreheures, entreminutes, entresecondes)
afficheTemps(demandeTemps()) 

def sommeTemps(temps1 : list,temps2: list):
    somme = tempsEnSeconde(temps1) + tempsEnSeconde(temps2)
    return secondeEnTemps(somme)
    
print(sommeTemps((2,3,4,25),(5,22,57,1)))


def proportionTemps(temps:list,proportion:int):
    return secondeEnTemps(secondeEnTemps(temps) * (proportion//100))
    
afficheTemps(proportionTemps((2,0,36,0),0.2))
#appeler la fonction en échangeant l'ordre des arguments



def tempsEnDate(temps):
    année = tempsEnSeconde(temps) // 31536000
    reste = tempsEnSeconde(temps) % 31536000
    jours = reste // 86400
    reste_2 = reste % 86400
    heures = reste_2 // 3600
    reste_3 = reste_2 % 3600
    minutes = reste_3 // 60
    secondes = reste_3 % 60
    tempsEnDate = année , jours , heures , minutes , secondes

def afficheDate(date = -1):
    if date[0] != 0 and date[0] > 1 :
        print(date[0], "années", end = " ")
    elif date[0] == 0 :
        print(date[0],"année",end = " ")
    elif date[1] != 0 and date[1] > 1 :
        print(date[1], "jours", end = " ")
    elif date[1] == 0 :
        print(date[1],"jour",end = " ")
    elif date[2] != 0 and date[2] > 1 :
        print(date[2], "heures", end = " ")
    elif date[2] == 0 :
        print(date[2],"heure",end = " ")
    elif date[3] != 0 and date[3] > 1 :
        print(date[3], "minutes", end = " ")
    elif date[3] == 0 :
        print(date[3],"minute",end = " ")
    elif date[4] != 0 and date[4] > 1 :
        print(date[4], "secondes", end = " ")
    elif date[4] == 0 :
        print(date[4],"seconde",end = " ")  
temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDate(temps))
afficheDate()

def nombreBisextile(jour: int):
    temps = (int(jour), 0, 0, 0)
    date = tempsEnDate(secondeEnTemps(tempsEnSeconde(temps)))
    annee = date[0]
    compteur = 0
    while annee != 0:
        if (annee % 4) == 0 and (annee % 100 != 0 or annee % 400 == 0):
            compteur += 1
        annee += -1
    return compteur


print(nombreBisextile(200000))

def tempsEnDateBisextile(temps):
    jours = temps[0]
    jours += nombreBisextile(temps)
    date = (0,jours, temps[1] , temps[2] ,temps[3])
    return date 

   
temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDateBisextile(temps))



def verifie(horaires):
    sommehoraire = 0
    for elem in horaires :
        print("l'employé a fait", elem[1]+ elem[0]*24, "heures dans la semaines")
        if tempsEnSeconde(elem) > (48*3600) or sommehoraire > (140 * 3600) :
            return print("l'employé a fait plus que la limite ")
    return print("il a fait moins que la limite")
 horaires = [[1,2,39,34],[0,1,9,4],[0,29,39,51],[0,31,13,46]]
verifie(horaires)
