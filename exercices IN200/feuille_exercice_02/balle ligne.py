import tkinter as tk
import random as rd
##################
# canvas.itemconfigure(cercle, fill="red")
##################
# Constantes

LARGEUR = 600
HAUTEUR = 400

aleatoire = 0
###################
# Fonctions


def creer_balle():
    """Dessine un disque bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    x, y = LARGEUR // 2, HAUTEUR // 2
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon-100, y-rayon-100),
                                (x+rayon-100, y+rayon-100),
                                fill="blue")
    return [cercle, dx, dy]


def mouvement():
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    rebond()
    canvas.move(balle[0], balle[1], balle[2])
    canvas.after(20, mouvement)


def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle, aleatoire

    if aleatoire <= 10:
        canvas.itemconfig(ligne, fill="black")
        t = 600
    else:
        t = 300
        canvas.itemconfig(ligne, fill="white")

    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0 or x1 >= t:
        balle[1] = -balle[1]
        aleatoire = rd.randint(0, 100)
        print(aleatoire)

    if y0 <= 0 or y1 >= 400:
        balle[2] = -balle[2]
        aleatoire = rd.randint(0, 100)
        print(aleatoire)


######################
# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()
#ligne
ligne = canvas.create_line((LARGEUR//2, 0), (LARGEUR//2, HAUTEUR), fill="white")
# initialisation de la balle
balle = creer_balle()

# déplacement de la balle
mouvement()

# boucle principale
racine.mainloop()
