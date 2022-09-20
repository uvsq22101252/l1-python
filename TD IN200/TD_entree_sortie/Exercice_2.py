import random


def nbr_lignes(nom_fichier):
    fic = open("words.txt", "r")
    somme = 0
    for _ in fic:
        somme += 1
    fic.close()
    return somme


print(nbr_lignes("words.txt"))


def ecrit_liste_mots(n):
    fic = open("words.txt", "r")
    fic_out = open("words" + str(n) + ".txt", "w")
    for ligne in fic:
        mot = ligne.strip()
        if len(mot) == n:
            fic_out.write(ligne)
    fic.close()
    fic_out.close()


ecrit_liste_mots(20)


def melange_mots(fichier):
    fic = open(fichier, "r")
    fic_out = open(fichier + "mel", "w")
    liste = fic.readlines()
    random.shuffle(liste)
    for mot in liste:
        fic_out.write(mot)
    fic.close
    fic_out.close


melange_mots("words.txt")


def compare_mots(m1, m2):
    n = len(m1)
    profil = [0] * n
    position = []
    for i in range(n):
        if m1[i] == m2[i]:
            profil[i] = 1
            position.append(i)
    for i in range(n):
        if profil != 1:
            l1 = m1[i]
            for j in range(n):
                if m2[j] == l1 and j not in position:
                    profil[i] = 2
                    position.append(j)
                    break
        return profil


compare_mots("anvil", )


def ecrit_liste_compatible(fichier, m, profil):
    fs = open(fichier + "comp", "w")
    fe = open(fichier, "r")
    for ligne in fe:
        mot = ligne.strip()
        if compare_mots(m, mot) == profil:
            fs.write(ligne)
    fs.close()
    fe.close()


ecrit_liste_compatible("words6.txt", "canard", [0, 0, 2, 0, 0, 0])
