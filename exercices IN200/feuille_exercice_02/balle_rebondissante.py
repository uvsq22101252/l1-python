import tkinter as tk
import random


# variable
liste_balle = []
arret = True
largeur = 600
hauteur = 400

# focntion


def creer_balle():  # fonction qui cree la balle au centre du canvas
    r = 20
    xb = largeur // 2
    yb = hauteur // 2
    cercle = canvas.create_oval(xb-r, yb-r, xb+r, yb+r, fill="blue")
    ax = random.randint(1, 7)
    ay = random.randint(1, 7)
    balle = [cercle, ax, ay]
    return balle


def mouvement_balle():
    global after
    rebond()
    canvas.move(balle[0], balle[1], balle[2])
    after = canvas.after(50, mouvement_balle)


def demarrer():
    global arret
    if arret:
        mouvement_balle()
        bouton.config(text="Arretez")
    else:
        canvas.after_cancel(after)
        bouton.config(text="Demarer")
    arret = not arret


def rebond():
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if y1 > hauteur or y0 < 0:
        balle[2] = -balle[2]
    if x1 > largeur or x0 < 0:
        balle[1] = -balle[1]


racine = tk.Tk()
titre = racine.title("Balle rebondissante")
canvas = tk.Canvas(height=hauteur, width=largeur, bg="black")
canvas.grid(row=0, column=0)
bouton = tk.Button(text="Démarrer", command=demarrer)
bouton.grid(row=1, column=0)

balle = creer_balle()

racine.mainloop()
