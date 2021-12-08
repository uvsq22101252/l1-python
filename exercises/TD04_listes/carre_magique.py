from typing import ContextManager


carre_mag= [[4,14,15,1],[9,7,6,12],[5,11,10,8],[16,2,3,13]]
#print(carre_mag[0])
#print(carre_mag[1])
#print(carre_mag[2])
#print(carre_mag[3])


carre_pas_mag = [[4,14,15,1],[9,7,6,12],[5,11,10,8],[16,2,7,13]]
#print(carre_pas_mag[0])
#print(carre_pas_mag[1])
#print(carre_pas_mag[2])
#print(carre_pas_mag[3])

def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    for i in range (0, len(carre)) :
        print(carre[i])
    print(" ")

afficheCarre(carre_mag)
afficheCarre(carre_pas_mag)

def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si toutes les lignes ont la même somme, et -1 sinon """
    chiffre = 0
    for i in range(0,len(carre)):
        somme = 0
        for n in range(0,4) :
            chiffre = (carre[i][n])
            somme += chiffre
            
            if i == 0 :
                somme_0 = somme
            elif i == 1 :
                somme_1 = somme 
            elif i == 2 :
                somme_2 = somme
            elif i == 3 :
                somme_3 = somme
          
    if somme_0 == somme_1 == somme_2 == somme_3 :
        return somme
    else : 
        return -1

print(testLignesEgales(carre_mag))
print(testLignesEgales(carre_pas_mag))


def testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre si toutes les colonnes ont la même somme, et -1 sinon """
    chiffre = 0
    somme = 0
    for n in range(0,4):
        somme = 0
        for i in range(0,4) :
            chiffre = (carre[i][n])
            somme += chiffre
            
            if  n == 0 :
                somme_0 = somme
            elif n == 1 :
                somme_1 = somme 
            elif n == 2 :
                somme_2 = somme
            elif n == 3 :
                somme_3 = somme
          
    if somme_0 == somme_1 == somme_2 == somme_3 :
        return somme_0
    else : 
        return -1

print(testColonnesEgales(carre_mag))
print(testColonnesEgales(carre_pas_mag))


def testDiagonalesEgales(carre):
    """ Renvoie la somme des éléments d'une diagonale de la liste 2D carre si les 2 diagonales ont la même somme, et -1 sinon """
    somme_1 = 0
    somme_2 = 0
    for i in range(0, 4 ) :
        for n in range (3 , -1, -1) :
            diagonale_1 = (carre[i][i])
            diagonale_2 = (carre[i][n])
        somme_1 += diagonale_1
        somme_2 += diagonale_2


    if somme_1 == somme_2:
        return somme_1
    else : 
        return -1


print(testDiagonalesEgales(carre_mag))
print(testDiagonalesEgales(carre_pas_mag))

def estCarreMagique(carre):
    """ Renvoie True si c'est un carre magique et False sinon"""
    if testLignesEgales(carre) == testColonnesEgales(carre) == testDiagonalesEgales(carre) :
       return True
    else :
        return False


print(estCarreMagique(carre_mag))
print(estCarreMagique(carre_pas_mag))


def estNormal(carre):
    """ Retourne True si contient toutes les valeurs de 1 à n^2 où n est la taille du carré, et False sinon """
    valeurs_du_carre = []
    liste_carre_magique =[]
    n = int(input("quelle est la taille du carré"))
    for i in range(1 , n**2 + 1 ):
        valeurs_du_carre.append(i)
    for a in range(0,4):
        for b in range (0,4) :
            liste_carre_magique.append(carre[a][b])

    
    liste_carre_magique.sort()
    print(valeurs_du_carre)
    print(liste_carre_magique)
    
    if valeurs_du_carre == liste_carre_magique :
        return True
    else :
        return False

print(estNormal(carre_mag))
print(estNormal(carre_pas_mag))