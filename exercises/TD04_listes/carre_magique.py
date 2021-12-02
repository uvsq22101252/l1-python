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
        print(somme)
    else : 
        print("-1")

#print(testLignesEgales(carre_mag))
#print(testLignesEgales(carre_pas_mag))


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
        print(somme_0)
    else : 
        print("-1")

print(testColonnesEgales(carre_mag))
print(testColonnesEgales(carre_pas_mag))