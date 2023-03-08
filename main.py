import tkinter as tk

mitarbeiter = tk.Tk()
mitarbeiter.title("MitarbeiterDatei")
mitarbeiter.minsize(width=600, height=300)
mitarbeiter.resizable(width=False, height=False)
#---------------------------------------------------------
#Frame und Widgets für die Eingabe
eingabeFrame = tk.Frame(width=200, height=298)
nummerEntry = tk.Entry(master=eingabeFrame, width=20, font="ComicSans")
vornameEntry = tk.Entry(master=eingabeFrame, width=20, font="ComicSans")
nachnameEntry = tk.Entry(master=eingabeFrame, width=20, font="ComicSans")
gebDatumEntry = tk.Entry(master=eingabeFrame, width=20, font="ComicSans")
vornameLabel = tk.Label(master=eingabeFrame, text="Vorname")
nachnameLabel = tk.Label(master=eingabeFrame, text="Nachname")
nummerLabel = tk.Label(master=eingabeFrame, text="Laufende Nummer")
gebDatumLabel = tk.Label(master=eingabeFrame, text="Geburtsdatum")
addButton = tk.Button(master=eingabeFrame, text="Hinzufügen" ,width=11)
searchButton = tk.Button(master=eingabeFrame,text="Suchen", width=11)

#---------------------------------------------------------
#Frame für Buttons und AnzigeListe der Personen
anzeigeFrame = tk.Frame(width=397, height=298)
anzeigeBox = tk.Listbox(master=anzeigeFrame)
anzeigeBox.place(x=5, y=5)


#---------------------------------------------------------
#PlaceBereich
nummerLabel.place(x=10, y=30)
nummerEntry.place(x=10, y=55)
vornameLabel.place(x=10, y=80)
vornameEntry.place(x=10, y=105)
nachnameLabel.place(x=10, y=130)
nachnameEntry.place(x=10, y=155)
gebDatumLabel.place(x=10, y=180)
gebDatumEntry.place(x=10, y=205)
addButton.place(x=10, y=245)
searchButton.place(x=108, y=245)


eingabeFrame.place(x=1, y=1)
anzeigeFrame.place(x=202, y=1)
mitarbeiter.mainloop()

# def add():



#
# window = tk.Tk()
# window.title("MitarbeiterDatei")
# window.minsize(width=800, height=600)
# window.resizable(width=False, height=False)
# hauptframe = tk.Frame(width=300, height=300, bg="red")
# zweitesFrame = tk.Frame(width=300, height=300)
# vorname = tk.Label(master=hauptframe, text="Vorname")
# vorname.pack()
# eingabe = tk.Entry(master=hauptframe)
# eingabe.pack()
# nachname = tk.Label(master=hauptframe, text="Nachname")
# nachname.pack()
# nameEingabe = tk.Entry(master=hauptframe)
# nameEingabe.pack()
# button_a = tk.Button(master=hauptframe, text="Hinzufügen")
# button_a.pack()
#
# label_a = tk.Label(master=hauptframe, text="frame A")
# label_a.pack()
#
# label_b = tk.Label(master=zweitesFrame, text="frame B")
# label_b.pack()
# hauptframe.place(x=50, y=75)
# zweitesFrame.pack()
#
#
# window.mainloop()
