liste_1 = [0, 1 ,2,3]
liste_2 = [4, 5 , 6, 7]

def intersection (liste_1 , liste_2) : 
    taille = len(liste_1)
    taille_2 = len(liste_2)
    intersection = []
    for i in range(0,taille+1):
        intersection = intersection.append(liste_1[i])
    for n in range(0, taille_2+1) :
        intersection = intersection.append(liste_2[n])
        print(intersection)

    print(intersection)