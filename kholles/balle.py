import tkinter as tk

from matplotlib.pyplot import fill

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400
compteur = 0
t = 0
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
    after = canvas.after(20, mouvement)
    canvas.move(ligne,-1,0)
    if compteur == 30:
        canvas.after_cancel(after)


def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle, t, compteur
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <=0 :
        balle[1] = -balle[1]
    
    if x1 >= (300):
        balle[1] = -balle[1]
        canvas.move(ligne,50,0)
        compteur += 1
    if y0 <= 0 or y1 >= 400:
        balle[2] = -balle[2]
        compteur +=1
    


######################
# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()

# initialisation de la balle
balle = creer_balle()
#ligne
ligne = canvas.create_line(((LARGEUR//2),0),((LARGEUR//2), HAUTEUR), fill="white")
# déplacement de la balle
mouvement()

# boucle principale
racine.mainloop()
