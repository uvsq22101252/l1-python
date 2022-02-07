import tkinter as tk

from numpy import blackman
#creation widgets
racine = tk.Tk()
racine.title("Le Roi du Sel")
bouton = tk.Button(text="recommencer",font=("Helvetica", "30"))
canvas = tk.Canvas(racine, height=500, width=500, bg="black")
canvas.grid(row=1, column=0)




racine.mainloop()
