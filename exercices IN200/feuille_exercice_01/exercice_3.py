import tkinter as tk 
#variable
compte_carre = 0
compte_cercle = 0
compte_croix = 0
historique = []
#fonction
def dessin(event):
    global compte_carre, compte_cercle, compte_croix, ligne_1, ligne_2, carre_1, carre_2, cercle_1
    x = event.x
    y = event.y
    
    if compte_croix < 2 and x < 166: 
        ligne_1 = canvas.create_line((x+30, y+30), (x-30, y-30), fill="blue")
        ligne_2 = canvas.create_line((x-30, y+30), (x+30, y-30), fill="blue")
        carre_1 = canvas.create_rectangle((x+30, y+30), (x-30, y-30), outline="white")
        compte_croix += 1
        historique.append(ligne_1)
        historique.append(ligne_2)
        historique.append(carre_1)
    elif compte_carre < 3 and x > 166 and x < 332:
        carre_2 = canvas.create_rectangle((x+30, y+30), (x-30, y-30), fill="green")
        compte_carre += 1
        historique.append(carre_2)
    elif compte_cercle < 4 and x > 332:
        cercle_1 = canvas.create_oval((x + 30, y + 30), (x - 30, y - 30), fill="red")
        compte_cercle += 1
        historique.append(cercle_1)

def Recommencer():
    global historique
    for i in range(0, len(historique)):
        canvas.delete(historique[i])
 
    compte_carre = 0
    compte_cercle = 0
    compte_croix = 0
    historique = []




racine = tk.Tk()
racine.title("le Rois du Sel")
canvas = tk.Canvas(racine, bg="black", height=500, width=500)
canvas.grid(column=0, row=0)
Bouton = tk.Button(text="Recommencer",command=Recommencer)
Bouton.grid(column=0, row=1)
racine.bind("<Button-1>", dessin)
ligne_1 = canvas.create_line((166, 0), (166, 500), fill="white")
ligne_2 = canvas.create_line((332, 0), (332, 500), fill="white")

racine.mainloop()