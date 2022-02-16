from tabnanny import check
from textwrap import fill
import tkinter as tk
from turtle import color
color = "blue"
check = True 

#creation event clique sur rectangle

def clique_rectangle(event):
    global color, check
    if check is not False:
        x = event.x
        y = event.y
        if x <= 100 and x >= 300 and y <= 100 and y >=300 :
            canvas.itemconfigure(rectangle, fill=color, outline="blue")
                if color == "blue" :
                    color = "red"
                else :
                    color ="blue"
        else :
            check=False
    return

#creation event recommencer

def recommencer(event):
    global check
    check = True
    return




#creation widgets
racine = tk.Tk()
racine.title("Le Roi du Sel")
bouton = tk.Button(text="recommencer",font=("Helvetica", "30"))
bouton.grid(row=2, column=0)
canvas = tk.Canvas(racine, height=500, width=500, bg="black")
rectangle = canvas.create_rectangle ((200, 200),(150, 150), fill="red")
canvas.grid(row=1, column=0)
racine.bind ("<Button-1>", clique_rectangle )


racine.mainloop()

