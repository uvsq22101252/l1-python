def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    boucle = 0
    liste_syracuse = []
    while n != 1:
        if n % 2 == 0 :
            n =  n // 2
            liste_syracuse.append(n) 
            boucle += 1

        else :
            n = (n * 3) + 1 
            liste_syracuse.append(n)
            boucle += 1

    print(boucle)    
    return(liste_syracuse)

print(syracuse(3))

def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """

    for i in range (2 , n_max) :
        liste_test_conjecture = syracuse(i)
        if liste_test_conjecture[len(liste_test_conjecture)-1] != 1 :
            print(liste_test_conjecture)
            return(False)
        else : 
            return(True)
            
    
    
print(testeConjecture(10000))

def tempsVol(n):
    """ Retourne le temps de vol de n """
    temps_de_Vol = 0
    while n != 1 :
        if n % 2 == 0 :
            n =  n // 2 
            temps_de_Vol += 1
        else :
            n = (n * 3) + 1 
            temps_de_Vol += 1
    return(temps_de_Vol)    

#print("Le temps de vol de", 3, "est", tempsVol(3))


def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    liste = []
    for n in range (1 , n_max+1) :
        liste.append(tempsVol(n))

    return(liste)  
#print(tempsVolListe(10000))


def altitude(n_max):
    """retourne l'altitude la plus grande avec son temps de vol """
    maximum = 0

    for n in range(1 , n_max+1) :
        list = syracuse(n)
        list.sort(reverse=True)
        if list[0] > maximum :
            maximum = list[0]
    
    
    return ("l'altitude la plus grande est ",syracuse(maximum), " et son temps de vol est ",tempsVol(maximum) )

#print(altitude(10000))
