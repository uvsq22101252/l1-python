import tkinter as tk
import random
#variable
balle = []
aleatoire = random.randint(0, 7)
#focntion
def creer_balle(): #fonction qui cree la balle au centre du canvas
    global cercle
    cercle = canvas.create_oval((180, 280), (220, 320), fill="blue")
    balle.append(aleatoire)

def mouvement_balle():
    cercle

racine = tk.Tk()
titre = racine.title("Balle rebondissante")
canvas = tk.Canvas(height=600, width=400, bg="black")
canvas.grid(row=0, column=0)
bouton = tk.Button(text="Démarrer", command=creer_balle)
bouton.grid(row=1, column=0)
print(canvas.coords(cercle))
racine.mainloop()

print(balle)
