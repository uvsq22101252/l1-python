import tkinter as tk
#variable
rectangle = 0
color = "red"
out =False
#fonction

def clique_rectangle(event):
    global rectangle, color, out
    x = event.x
    y = event.y
    if out == False:
        if x > 100 and x < 300 and y > 100 and y < 200 and color == "red" and out == False:
            color = "blue"
            rectangle = canvas.create_rectangle ((100, 100), (300, 200), fill=color)
        elif x > 100 and x < 300 and y > 100 and y < 200 and color == "blue" and out == False:
            color = "red"
            rectangle = canvas.create_rectangle((100, 100), (300, 200), fill=color)
        else : 
            out =True
    
def recommencer():
    global out
    out = False









racine = tk.Tk()
racine.title("Le Roi du Sel")
bouton = tk.Button(text="recommencer", font=("Helvetica", "30"),command=recommencer)
bouton.grid(row=2, column=0)
canvas = tk.Canvas(racine, height=500, width=500, bg="black")
rectangle = canvas.create_rectangle((100, 100), (300, 200), fill=color)
canvas.grid(row=1, column=0)
racine.bind("<Button-1>", clique_rectangle)


racine.mainloop()
