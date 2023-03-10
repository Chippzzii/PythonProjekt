import tkinter as tk
from tkinter import ttk, END
import mysql.connector


def mitarbeiterGUI():
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

        if (datenbank,) in data:
            print("Datenbank ist vorhanden.")
            db = mysql.connector.Connect(
                host="localhost",
                user="root",
                password="",
                database="mitarbeiter_db"
            )
            cursor = db.cursor()

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
                    treeview.insert("", "end", text=str(i + 1), values=row)

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

            def doppelteDaten(self):
                vorname = self.vornameEntry.get()
                nachname = self.nachnameEntry.get()
                gebDatum = self.gebDatumEntry.get()
                sql = "SELECT * FROM mitarbeiter WHERE Vorname = %s AND Nachname = %s AND Geburtsdatum = %s"
                cursor.execute(sql, (vorname, nachname, gebDatum))
                ergebnis = cursor.fetchone()
                if ergebnis:
                    return True
                else:
                    return False

            def searchPlatzhalter(self):
                platzhalter = []
                for mitarbeiter in cursor:
                    platzhalter.append(mitarbeiter)
                for i in range(0, len(platzhalter), 1):
                    persNummer = platzhalter[i][0]
                    vorname = platzhalter[i][1]
                    nachname = platzhalter[i][2]
                    gebDatum = platzhalter[i][3]
                    self.tree.insert('', i, values=(persNummer, vorname, nachname, gebDatum))

            class gui:
                def addButtonAction(self):
                    if (self.nachnameEntry.get() == ""):
                        print("Leere Eingabe")
                    else:
                        if (doppelteDaten(self)):
                            print("Datensatz ist bereits vorhanden.")
                        else:
                            addData(self)
                            updateListe(self)

                def searchButtonAction(self):
                    deleteAll(self)
                    if self.vornameEntry.get() and self.nachnameEntry.get():
                        vorname = self.vornameEntry.get()
                        nachname = self.nachnameEntry.get()
                        sql = "SELECT * FROM mitarbeiter WHERE Vorname = %s and Nachname = %s"
                        cursor.execute(sql, (vorname, nachname))
                        searchPlatzhalter(self)

                    elif self.vornameEntry.get() and self.gebDatumEntry.get():
                        vorname = self.vornameEntry.get()
                        gebDatum = self.gebDatumEntry.get()
                        sql = "SELECT * FROM mitarbeiter WHERE Vorname = %s and Geburtsdatum = %s"
                        cursor.execute(sql, (vorname, gebDatum))
                        searchPlatzhalter(self)

                    elif self.nachnameEntry.get() and self.gebDatumEntry.get():
                        nachname = self.nachnameEntry.get()
                        gebDatum = self.gebDatumEntry.get()
                        sql = "SELECT * FROM mitarbeiter WHERE Nachname = %s and Geburtsdatum = %s"
                        cursor.execute(sql, (nachname, gebDatum))
                        searchPlatzhalter(self)

                    elif self.nummerEntry.get():
                        nummer = self.nummerEntry.get()
                        sql = "SELECT * FROM mitarbeiter WHERE PersonalNr = %s"
                        cursor.execute(sql, (nummer))
                        searchPlatzhalter(self)

                    elif self.vornameEntry.get() or self.nachnameEntry.get() or self.gebDatumEntry.get():
                        nummer = self.nummerEntry.get()
                        vorname = self.vornameEntry.get()
                        nachname = self.nachnameEntry.get()
                        gebDatum = self.gebDatumEntry.get()
                        sql = "SELECT * FROM mitarbeiter WHERE PersonalNr = %s OR Vorname = %s OR Nachname = %s OR Geburtsdatum = %s"
                        values = nummer, vorname, nachname, gebDatum
                        cursor.execute(sql, values)
                        searchPlatzhalter(self)
                    else:
                        sql = "SELECT * FROM mitarbeiter"
                        cursor.execute(sql)
                        searchPlatzhalter(self)

                    self.nummerEntry.delete(0, END)
                    self.vornameEntry.delete(0, END)
                    self.nachnameEntry.delete(0, END)
                    self.gebDatumEntry.delete(0, END)

                def saveButtonAction(self):
                    if (self.nummerEntry.get()):
                        nummer = self.nummerEntry.get()
                        vorname = self.vornameEntry.get()
                        nachname = self.nachnameEntry.get()
                        gebDatum = self.gebDatumEntry.get()
                        sql = "UPDATE mitarbeiter SET Vorname = '%s', Nachname = '%s', Geburtsdatum = '%s' WHERE PersonalNr = %s"
                        cursor.execute(sql % (vorname, nachname, gebDatum, nummer))
                        cursor.execute("COMMIT;")
                        self.nummerEntry.delete(0, END)
                        self.vornameEntry.delete(0, END)
                        self.nachnameEntry.delete(0, END)
                        self.gebDatumEntry.delete(0, END)
                        updateListe(self)
                    else:
                        print("Leere Felder")

                def deleteButtonAction(self):
                    if (self.nummerEntry.get()):
                        nummer = self.nummerEntry.get()
                        sql = "DELETE from mitarbeiter WHERE PersonalNr = %s"
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
                    mitarbeiter.minsize(width=600, height=400)
                    mitarbeiter.resizable(width=False, height=False)
                    # ---------------------------------------------------------
                    # Frame und Widgets für die Eingabe
                    datenbankFrame = tk.Frame(width=300, height=75)
                    self.datenbankEntry = tk.Entry(master=datenbankFrame, width=20, font="ComicSans")
                    self.datenbankEingabeLabel = tk.Label(master=datenbankFrame, text="Datenbank")
                    # ---------------------------------------------------------
                    # Frame und Widgets für die Eingabe
                    eingabeFrame = tk.Frame(width=200, height=348)
                    # master bestimmt zugehörigkeit
                    self.nummerEntry = tk.Entry(master=eingabeFrame, width=20, font="ComicSans")  # Schriftart bestimmt größe des Entry Fensters
                    self.vornameEntry = tk.Entry(master=eingabeFrame, width=20, font="ComicSans")
                    self.nachnameEntry = tk.Entry(master=eingabeFrame, width=20, font="ComicSans")
                    self.gebDatumEntry = tk.Entry(master=eingabeFrame, width=20, font="ComicSans")
                    vornameLabel = tk.Label(master=eingabeFrame, text="Vorname")
                    nachnameLabel = tk.Label(master=eingabeFrame, text="Nachname")
                    nummerLabel = tk.Label(master=eingabeFrame, text="PersonalNr")
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

                    self.datenbankEingabeLabel.place(x=10, y=15)
                    self.datenbankEntry.place(x=10, y=40)


                    datenbankFrame.place(x=1, y=1)
                    eingabeFrame.place(x=1, y=76)
                    anzeigeFrame.place(x=202, y=76)
                    inTreviewSchreiben(self.tree)
                    mitarbeiter.mainloop()

            dbms.close()

        else:
            print("datenbank nicht gefunden")
            dbms = mysql.connector.Connect(
                host="localhost",
                user="root",
                password=""
            )
            zeiger = dbms.cursor()
            sql = "CREATE DATABASE mitarbeiter_db;"
            sqlZwei = "CREATE TABLE mitarbeiter_db.mitarbeiter(PersonalNr int(11) NOT NULL,Vorname VARCHAR(50),Nachname VARCHAR(50) NOT NULL,Geburtsdatum DATE,PRIMARY KEY (PersonalNr));"
            zeiger.execute(sql)
            zeiger.execute(sqlZwei)
            dbms.close()
            zeiger.close()
            mitarbeiterGUI()

    except mysql.connector.Error as err:
        print("Fehler beim Verbinden zur Datenbank!")
        print(err)

    gui()


mitarbeiterGUI()
