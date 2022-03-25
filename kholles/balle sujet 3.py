import tkinter as tk



##################
# Constantes

LARGEUR = 600
HAUTEUR = 400
compteur = 0

###################
# Fonctions

def creer_balle():
    global cercle
    """Dessine un disque bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    x, y = LARGEUR // 2, HAUTEUR // 2
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="blue")
    return [cercle, dx, dy]


def mouvement():
    global after
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    rebond()
    canvas.move(balle[0], balle[1], balle[2])
    after = canvas.after(20, mouvement)
    if compteur == 3:
        canvas.after_cancel(after)


def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle, compteur
    x0, y0, x1, y1 = canvas.coords(balle[0])
    
    if x0 <= 0 or x1 >= 600:
        balle[1] = -balle[1]
        compteur += 1
    if y0 <= 0 or y1 >= 400:
        balle[2] = -balle[2]
        compteur += 1
    
    if   (x0 or x1) <=10:
        canvas.itemconfig(cercle, fill="yellow")
        
    if  (x0 and x1 )<=600 and (y0 and y1) ==0 :
        canvas.itemconfig(cercle, fill="red")
        
    if  (x0 and x1) <=600 and (y0 and y1) == 400:
        canvas.itemconfig(cercle, fill="blue")
        
    if  (x0 and x1) >= 590:
        canvas.itemconfig(cercle, fill="green")
        
    

             
            
   
   
######################
# programme principal


# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()
#ligne
rouge=canvas.create_line((0,0),(600,0), fill="red", width=10)
canvas.create_line((600,0),(600, 400), fill="green", width=10)
canvas.create_line((0,400),(600, 400),fill="blue", width=10)
canvas.create_line((0,0),(0,400),fill="yellow", width=10)
stop = tk.Button(text="stop", command= lambda: canvas.after_cancel(after))
stop.grid(row=3)
# initialisation de la balle

balle = creer_balle()

# déplacement de la balle
mouvement()

# boucle principale
racine.mainloop()
