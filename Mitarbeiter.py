import tkinter as tk
from tkinter import ttk, END

import mysql.connector

db = mysql.connector.Connect(
    host="localhost",
    user="root",
    password="",
    database="mitarbeiter_db"
)
cursor = db.cursor()


class gui:

    def addButtonAction(self):
        # nummer = self.nummerEntry.get()
        vorname = self.vornameEntry.get()
        nachname = self.nachnameEntry.get()
        gebDatum = self.gebDatumEntry.get()
        print("Daten:", vorname, nachname, gebDatum)
        self.nummerEntry.delete(0, END)
        self.vornameEntry.delete(0, END)
        self.nachnameEntry.delete(0, END)
        self.gebDatumEntry.delete(0, END)
        sql = "INSERT INTO mitarbeiter(Vorname, Nachname, Geburtsdatum) VALUES(%s, %s, %s)"
        # parameter mit Komma trennen, bei Update und Delete % execute(sql, (daten))
        cursor.execute(sql, (vorname, nachname, gebDatum))
        # Daten in DB schreiben/ übertragen
        cursor.execute("COMMIT;")

    def searchButtonAction(self):
        if self.nummerEntry.get():
            nummer = self.nummerEntry.get()
            sql = "SELECT * FROM mitarbeiter WHERE PersonalNr = " + nummer
            cursor.execute(sql)
            platzhalter = []
            for mitarbeiter in cursor:
                print(mitarbeiter)
                platzhalter.append(mitarbeiter)

            persNummer = platzhalter[0][0]
            vorname = platzhalter[0][1]
            nachname = platzhalter[0][2]
            gebDatum = platzhalter[0][3]

            print(persNummer, vorname, nachname, gebDatum)



    def __init__(self):
        mitarbeiter = tk.Tk()
        mitarbeiter.title("MitarbeiterDatei")
        mitarbeiter.minsize(width=600, height=325)
        mitarbeiter.resizable(width=False, height=False)
        # ---------------------------------------------------------
        # Frame und Widgets für die Eingabe
        eingabeFrame = tk.Frame(width=200, height=348)

        self.nummerEntry = tk.Entry(master=eingabeFrame, width=20, font="ComicSans")
        self.vornameEntry = tk.Entry(master=eingabeFrame, width=20, font="ComicSans")
        self.nachnameEntry = tk.Entry(master=eingabeFrame, width=20, font="ComicSans")
        self.gebDatumEntry = tk.Entry(master=eingabeFrame, width=20, font="ComicSans")
        vornameLabel = tk.Label(master=eingabeFrame, text="Vorname")
        nachnameLabel = tk.Label(master=eingabeFrame, text="Nachname")
        nummerLabel = tk.Label(master=eingabeFrame, text="Laufende Nummer")
        gebDatumLabel = tk.Label(master=eingabeFrame, text="Geburtsdatum")
        addButton = tk.Button(master=eingabeFrame, text="Hinzufügen", width=11, command=self.addButtonAction)
        searchButton = tk.Button(master=eingabeFrame, text="Suchen", width=11, command=self.searchButtonAction)
        saveButton = tk.Button(master=eingabeFrame, text="Speichern", width=11)
        deleteButton = tk.Button(master=eingabeFrame, text="Löschen", width=11)

        # ---------------------------------------------------------
        # Frame für Buttons und AnzigeListe der Personen
        anzeigeFrame = tk.Frame(width=397, height=348)
        columns = ('Nummer', 'Vorname', 'Nachname', 'Geburtsdatum')
        tree = ttk.Treeview(master=anzeigeFrame, columns=columns, show='headings', height=12)
        tree.heading('Nummer', text='Nummer', anchor='w')
        tree.heading('Vorname', text='Vorname', anchor='w')
        tree.heading('Nachname', text='Nachname', anchor='w')
        tree.heading('Geburtsdatum', text='Geburtsdatum', anchor='w')
        tree.column('#1', width=90)
        tree.column('#2', width=90)
        tree.column('#3', width=95)
        tree.column('#4', width=110)
        tree.insert('', '0', text="Christian",
                    values=('1', "Christian", "Hülsmann", "Juli"))  # insert durch Funktion ersetzen

        # ---------------------------------------------------------
        # PlaceBereich
        nummerLabel.place(x=10, y=30)
        self.nummerEntry.place(x=10, y=55)
        vornameLabel.place(x=10, y=80)
        self.vornameEntry.place(x=10, y=105)
        nachnameLabel.place(x=10, y=130)
        self.nachnameEntry.place(x=10, y=155)
        gebDatumLabel.place(x=10, y=180)
        self.gebDatumEntry.place(x=10, y=205)
        addButton.place(x=10, y=245)
        searchButton.place(x=108, y=245)
        saveButton.place(x=10, y=275)
        deleteButton.place(x=108, y=275)
        tree.place(x=5, y=35)

        eingabeFrame.place(x=1, y=1)
        anzeigeFrame.place(x=202, y=1)
        mitarbeiter.mainloop()


gui()
