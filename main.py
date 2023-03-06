import tkinter as tk

window = tk.Tk()
window.title("MitarbeiterDatei")
window.minsize(width=800, height=600)
window.resizable(width=False, height=False)
hauptframe = tk.Frame(width=300, height=300, bg="red")
zweitesFrame = tk.Frame(width=300, height=300)
vorname = tk.Label(master=hauptframe, text="Vorname")
vorname.pack()
eingabe = tk.Entry(master=hauptframe)
eingabe.pack()
nachname = tk.Label(master=hauptframe, text="Nachname")
nachname.pack()
nameEingabe = tk.Entry(master=hauptframe)
nameEingabe.pack()
button_a = tk.Button(master=hauptframe, text="Hinzufügen")
button_a.pack()

label_a = tk.Label(master=hauptframe, text="frame A")
label_a.pack()

label_b = tk.Label(master=zweitesFrame, text="frame B")
label_b.pack()
hauptframe.place(x=50, y=75)
zweitesFrame.pack()


window.mainloop()
