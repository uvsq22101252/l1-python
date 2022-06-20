import tkinter as tk
##fonction


def creer_balle():
    Canvas.create_oval(200, 200, 300, 300, fill="blue")

def 




## interface graphique


racine = tk.Tk()
racine.title("Projet")

Canvas = tk.Canvas(racine, width=500, height=500, bg='black')
Canvas.grid(row=0, column=0)
Bquitter = tk.Button(racine, text='Quit', command=racine.quit)
Bquitter.grid(row=1, column=1)
Bcreer_balle = tk.Button(racine, text='Commencer', command=creer_balle)
Bcreer_balle.grid(row=2, column=1)

##fonction interface graphique





racine.mainloop()