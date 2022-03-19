somme = 0
moyenne = 0

fic = open("notes.txt", "r")
fic_out = open("moyenne.txt", "w")

for ligne in fic:
    liste = ligne.split()
    somme = int(liste[1]) + int(liste[2]) + int(liste[3])
    moyenne = int(somme/3)
    fic_out.write(str(liste[0]) + " " + str(liste[1]) + " " + str(liste[2]) + " " + str(liste[3]) + " " + str(moyenne) + "\n")

fic.close()
fic_out.close()