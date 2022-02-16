import tkinter as tk
#variables
compte = 0
ligne_1 = 0
ligne_2 = 0
verif = True
#fonction

def stop():
    global verif
    if verif is True :
        verif = False
        Bouton['text'] = "recommencer"
    else :
        verif = True
        Bouton['text'] = "Pause"
    return


def ligne_1(event):
    global ligne_01
    ligne_01 = canvas.create_line((0,100),(100,100),fill="blue")

def ligne_2(event):
    global ligne_02
    ligne_02 = canvas.create_line((100,100),(200,100),fill="red")

def nbr_clique(event):
    if verif is True :
        global compte
        compte += 1

        if compte == 2 :
            ligne_1(event)
        elif compte == 4 :
            ligne_2(event)
        elif compte > 4 :
            canvas.delete(ligne_01, ligne_02)
            compte = 0

racine = tk.Tk()
racine.title("le Rois du Sel")
canvas = tk.Canvas(racine, bg="white", height=500, width=500)
canvas.grid(column=0, row=0)
Bouton = tk.Button(text="Pause", command=stop)
Bouton.grid(column=0,row=1)
racine.bind("<Button-1>", nbr_clique)







racine.mainloop()