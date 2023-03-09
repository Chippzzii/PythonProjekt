import tkinter as tk
from tkinter import ttk, END
import mysql.connector

try:
    dbms = mysql.connector.Connect(
        host="localhost",
        user="root",
        password=""
    )
    zeiger = dbms.cursor()
    zeiger.execute("SHOW DATABASES")
    data = zeiger.fetchall()
    datenbank = "mitarbeiter_db"
    # for db in data:
    #     print(db)
    for daten in data:
        if datenbank in daten:
            print("Datenbank ist vorhanden.")
            db = mysql.connector.Connect(
                            host="localhost",
                            user="root",
                            password="",
                            database="mitarbeiter_db"
                            )
            cursor = db.cursor()
            break
        else:
            print("Datenbank nicht gefunden, wird neu erstellt.")
                # CREATE DATABASE mitarbeiter_db;
                # CREATE TABLE mitarbeiter_db.mitarbeiter(
                # PersonalNr int(11) NOT NULL,
                # Vorname VARCHAR(50),
                # Nachname VARCHAR(50) NOT NULL,
                # Geburtsdatum DATE,
                # PRIMARY KEY (PersonalNr)
                # );



except mysql.connector.Error as err:
    print("Fehler beim Verbinden zur Datenbank!")
    print(err)

def deleteAll(self):
    for item in self.tree.get_children():
        if item != '':
            self.tree.delete(item)

def preLoadData():
    sql = "SELECT * FROM mitarbeiter"
    cursor.execute(sql)
    column_names = [description[0] for description in cursor.description]
    data = [row for row in cursor]
    return column_names, data

def inTreviewSchreiben(treeview):
    column_names, data = preLoadData()
    for i, row in enumerate(data):
        treeview.insert("", "end", text=str(i+1), values=row)

def addData(self):
    vorname = self.vornameEntry.get()
    nachname = self.nachnameEntry.get()
    gebDatum = self.gebDatumEntry.get()
    print("Daten:", vorname, nachname, gebDatum)
    self.nummerEntry.delete(0, END)
    self.vornameEntry.delete(0, END)
    self.nachnameEntry.delete(0, END)
    self.gebDatumEntry.delete(0, END)
    sql = "INSERT INTO mitarbeiter(Vorname, Nachname, Geburtsdatum) VALUES(%s, %s, %s)"
    cursor.execute(sql, (vorname, nachname, gebDatum))
    cursor.execute("COMMIT;")

def updateListe(self):
    deleteAll(self)
    preLoadData()
    inTreviewSchreiben(self.tree)


class gui:
    def addButtonAction(self):
        # ToDo: Überprüfung auf Doppelte Datensätze
        if(self.nachnameEntry.get() == ""):
            print("Leere Eingabe")
        else:
            addData(self)
            updateListe(self)
    def searchButtonAction(self):
        deleteAll(self)
        if self.nummerEntry.get():
            nummer = self.nummerEntry.get()
            sql = "SELECT * FROM mitarbeiter WHERE PersonalNr = " + nummer
            cursor.execute(sql)
            platzhalter = []
            for mitarbeiter in cursor:
                platzhalter.append(mitarbeiter)
            for i in range(0, len(platzhalter), 1):
                persNummer = platzhalter[i][0]
                vorname = platzhalter[i][1]
                nachname = platzhalter[i][2]
                gebDatum = platzhalter[i][3]
                self.tree.insert('', i, values=(persNummer, vorname, nachname, gebDatum))

        elif self.vornameEntry.get():
            vorname = self.vornameEntry.get()
            sql = "SELECT * FROM mitarbeiter WHERE Vorname = '" + vorname + "'"
            cursor.execute(sql)
            platzhalter = []
            for mitarbeiter in cursor:
                platzhalter.append(mitarbeiter)
            for i in range(0, len(platzhalter), 1):
                persNummer = platzhalter[i][0]
                vorname = platzhalter[i][1]
                nachname = platzhalter[i][2]
                gebDatum = platzhalter[i][3]
                self.tree.insert('', i, values=(persNummer, vorname, nachname, gebDatum))

        elif self.nachnameEntry.get():
            nachname = self.nachnameEntry.get()
            sql = "SELECT * FROM mitarbeiter WHERE Nachname = '" + nachname + "'"
            cursor.execute(sql)
            platzhalter = []
            for mitarbeiter in cursor:
                platzhalter.append(mitarbeiter)
            for i in range(0, len(platzhalter), 1):
                persNummer = platzhalter[i][0]
                vorname = platzhalter[i][1]
                nachname = platzhalter[i][2]
                gebDatum = platzhalter[i][3]
                self.tree.insert('', i, values=(persNummer, vorname, nachname, gebDatum))

        elif self.gebDatumEntry.get():
            gebDatum = self.gebDatumEntry.get()
            sql = "SELECT * FROM mitarbeiter WHERE Geburtsdatum = '" + gebDatum + "'"
            cursor.execute(sql)
            platzhalter = []
            for mitarbeiter in cursor:
                platzhalter.append(mitarbeiter)
            for i in range(0, len(platzhalter), 1):
                persNummer = platzhalter[i][0]
                vorname = platzhalter[i][1]
                nachname = platzhalter[i][2]
                gebDatum = platzhalter[i][3]
                self.tree.insert('', i, values=(persNummer, vorname, nachname, gebDatum))
        else:
            sql = "SELECT * FROM mitarbeiter"
            cursor.execute(sql)
            platzhalter = []
            for mitarbeiter in cursor:
                platzhalter.append(mitarbeiter)

            for i in range(0, len(platzhalter), 1):
                persNummer = platzhalter[i][0]
                vorname = platzhalter[i][1]
                nachname = platzhalter[i][2]
                gebDatum = platzhalter[i][3]
                self.tree.insert('', i, values=(persNummer, vorname, nachname, gebDatum))

        self.nummerEntry.delete(0, END)
        self.vornameEntry.delete(0, END)
        self.nachnameEntry.delete(0, END)
        self.gebDatumEntry.delete(0, END)

    def saveButtonAction(self):
        if(self.nummerEntry.get()):
            nummer = self.nummerEntry.get()
            vorname = self.vornameEntry.get()
            nachname = self.nachnameEntry.get()
            gebDatum = self.gebDatumEntry.get()
            sql = "UPDATE mitarbeiter SET Vorname = '%s', Nachname = '%s', Geburtsdatum = '%s' WHERE PersonalNr = " + nummer
            cursor.execute(sql % (vorname, nachname, gebDatum))
            cursor.execute("COMMIT;")
            self.nummerEntry.delete(0, END)
            self.vornameEntry.delete(0, END)
            self.nachnameEntry.delete(0, END)
            self.gebDatumEntry.delete(0, END)
            updateListe(self)
        else:
            print("Leere Felder")

    def deleteButtonAction(self):
        if(self.nummerEntry.get()):
            nummer = self.nummerEntry.get()
            sql = "DELETE from mitarbeiter WHERE PersonalNr = %s"
            print(sql % (nummer))
            cursor.execute(sql % (nummer))
            cursor.execute("COMMIT;")
            self.nummerEntry.delete(0, END)
            self.vornameEntry.delete(0, END)
            self.nachnameEntry.delete(0, END)
            self.gebDatumEntry.delete(0, END)
            updateListe(self)
        else:
            print("Leere Zeile!")

    def treeSelection(self, event):
        temp = self.tree.selection()[0]
        platzhalter = self.tree.item(temp, 'values')
        self.nummerEntry.delete(0, END)
        self.vornameEntry.delete(0, END)
        self.nachnameEntry.delete(0, END)
        self.gebDatumEntry.delete(0, END)
        self.nummerEntry.insert(0, platzhalter[0])
        self.vornameEntry.insert(0, platzhalter[1])
        self.nachnameEntry.insert(0, platzhalter[2])
        self.gebDatumEntry.insert(0, platzhalter[3])

    def __init__(self):
        mitarbeiter = tk.Tk()
        mitarbeiter.title("MitarbeiterDatei")
        mitarbeiter.minsize(width=600, height=325)
        mitarbeiter.resizable(width=False, height=False)
        # ---------------------------------------------------------
        # Frame und Widgets für die Eingabe
        eingabeFrame = tk.Frame(width=200, height=348)
        #master bestimmt zugehörigkeit
        self.nummerEntry = tk.Entry(master=eingabeFrame, width=20, font="ComicSans") #Schriftart bestimmt größe des Entry Fensters
        self.vornameEntry = tk.Entry(master=eingabeFrame, width=20, font="ComicSans")
        self.nachnameEntry = tk.Entry(master=eingabeFrame, width=20, font="ComicSans")
        self.gebDatumEntry = tk.Entry(master=eingabeFrame, width=20, font="ComicSans")
        vornameLabel = tk.Label(master=eingabeFrame, text="Vorname")
        nachnameLabel = tk.Label(master=eingabeFrame, text="Nachname")
        nummerLabel = tk.Label(master=eingabeFrame, text="Laufende Nummer")
        gebDatumLabel = tk.Label(master=eingabeFrame, text="Geburtsdatum")
        addButton = tk.Button(master=eingabeFrame, text="Hinzufügen", width=11, command=self.addButtonAction)
        searchButton = tk.Button(master=eingabeFrame, text="Suchen", width=11, command=self.searchButtonAction)
        saveButton = tk.Button(master=eingabeFrame, text="Speichern", width=11, command=self.saveButtonAction)
        deleteButton = tk.Button(master=eingabeFrame, text="Löschen", width=11, command=self.deleteButtonAction)

        # ---------------------------------------------------------
        # Frame für Buttons und AnzigeListe der Personen
        anzeigeFrame = tk.Frame(width=397, height=348)
        columns = ('Nummer', 'Vorname', 'Nachname', 'Geburtsdatum')
        self.tree = ttk.Treeview(master=anzeigeFrame, columns=columns, show='headings', height=12, selectmode='browse')
        self.tree.bind('<Double-1>', self.treeSelection)
        self.tree.heading('Nummer', text='Nummer', anchor='w')
        self.tree.heading('Vorname', text='Vorname', anchor='w')
        self.tree.heading('Nachname', text='Nachname', anchor='w')
        self.tree.heading('Geburtsdatum', text='Geburtsdatum', anchor='w')
        self.tree.column('#1', width=90)
        self.tree.column('#2', width=90)
        self.tree.column('#3', width=95)
        self.tree.column('#4', width=110)

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
        self.tree.place(x=5, y=35)
        eingabeFrame.place(x=1, y=1)
        anzeigeFrame.place(x=202, y=1)
        # inTreviewSchreiben(self.tree)
        mitarbeiter.mainloop()

gui()