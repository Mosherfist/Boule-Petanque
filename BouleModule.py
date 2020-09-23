import os
import random
import sqlite3


def turnier_menue():
    print(
        "1:\tDatenbank auswählen\n2:\tTeilnehmer eingeben\n3:\tTeilnehmer anzeigen\n4:\tTabelle abfragen\n5:\tAuslosung Runde 1\nq:\tProgramm beenden\n\tIhre Eingabe: ")
    eingabe = input()
    if eingabe == "1":
        datenbank_erstellen()
    if eingabe == "2":
        teilnehmer_eingeben(datenbank_name)
    if eingabe == "3":
        teilnehmer_abfragen(datenbank_name)
    if eingabe == "4":
        tabelle_abfragen(datenbank_name)
    if eingabe == "5":
        turnier_auslosung(datenbank_name)
    if eingabe == "q":
        print("Das Programm wird beendet ! Bis zum nächsten Mal !")
        quit()

    else:
        turnier_menue()


def datenbank_erstellen():
    global datenbank_name
    datenbank_name = input("Datenbanknamen bestimmen: ")
    if os.path.exists(datenbank_name + ".db"):
        print("Datenbank bereits vorhanden ! Es wird in alter Turnierdatenbank " + datenbank_name + ".db gespielt !")
        turnier_menue()


    else:

        print("Erstelle neue Turnierdatenbank und die zugehörigen Tabellen...")
        conn = sqlite3.connect(datenbank_name + ".db")
        c = conn.cursor()
        c.execute(
            "CREATE TABLE Teilnehmer (Team_ID INTEGER Primary Key, Teamname TEXT, Aktiv INTEGER, Freilos INTEGER, gewonnene_Spiele INTEGER, Punkte INTEGER)")
        c.execute(
            " CREATE TABLE Spielablauf (Spiel_ID INTEGER PRIMARY KEY, Runde INTEGER, Gegner_1 INTEGER, Gegner_2 INTEGER, Gewinner INTEGER, Punkte_G1 INTEGER, Punkte_G2 INTEGER, Status Text)")
        conn.commit()
        conn.close()
        print("Datenbank " + datenbank_name + ".db " + "und Tabellen erfolgreich erstellt")
        turnier_menue()


def tabelle_abfragen(datenbank_name):
    stand = []
    conn = sqlite3.connect(datenbank_name + ".db")
    c = conn.cursor()
    c.execute(""" SELECT Teamname,  gewonnene_Spiele, Punkte FROM Teilnehmer ORDER by Punkte DESC """)
    tabelle = c.fetchall()
    for i in tabelle:
        Teamname, gewonnene_Spiele, Punkte = i
        print("Teamname: " + Teamname + "\t \tgewonnene Spiele: " + str(gewonnene_Spiele) + "\tPunkte: " + str(Punkte))
        stand.append(i)
    conn.close()
    turnier_menue()


def teilnehmer_eingeben(datenbank_name):
    Teamname = input("Bitte den Teamnamen eingeben. Um die Eingabe zu beenden  `q` eingeben: ")
    if Teamname == "q":
        turnier_menue()
    else:
        entscheidung = input(Teamname + " korrekt ? j = ja, n = nein: ")
        if entscheidung == "j":
            conn = sqlite3.connect(datenbank_name + ".db")
            c = conn.cursor()
            c.execute(
                """INSERT into Teilnehmer (Teamname, Aktiv, Freilos, gewonnene_Spiele, Punkte) Values(?, ?, ?, ?, ?)""",
                (Teamname, 0, 0, 0, 0))
            conn.commit()
            print("Team " + Teamname + " hinzugefügt")
            teilnehmer_eingeben(datenbank_name)
        elif entscheidung == "n":
            print("Erneut eingeben !")
            teilnehmer_eingeben(datenbank_name)
        else:
            print("Fehlerhafte Eingabe. Sie werden zurück ins Menü geführt...")
            turnier_menue()


def teilnehmer_abfragen(datenbank_name):
    conn = sqlite3.connect(datenbank_name + ".db")
    c = conn.cursor()
    c.execute("""SELECT Team_ID, Teamname FROM Teilnehmer """)
    Teilnehmer = c.fetchall()
    conn.close()
    for i in Teilnehmer:
        Team_ID, Teamname = i
        print("TeamID: " + str(Team_ID) + " Teamname: " + Teamname)
    turnier_menue()


def ergebnis_eintragen(datenbank_name, Spiel_ID):
    conn = sqlite3.connect(datenbank_name + ".db")
    c = conn.cursor()
    c.execute(""" SELECT Spiel_ID, Gegner_1, Gegner_2 FROM Spielablauf WHERE Status = "läuft" """)
    laufende_spiele = c.fetchall()
    for i in laufende_spiele:
        print(laufende_spiele)
        Spiel_ID, Gegner_1, Gegner_2 = i
        c.execute("SELECT Teamname FROM Teilnehmer WHERE Team_ID = ? ", (str(Gegner_1)))
        Gegner_1 = c.fetchall()
        c.execute(" SELECT Teamname FROM Teilnehmer WHERE Team_ID = ? ", (str(Gegner_2)))
        Gegner_2 = c.fetchall()
        print(Spiel_ID, Gegner_1, Gegner_2)
    conn.close()


def datenbanken_auslesen():
    datenbanken = []
    for i in os.listdir():
        if i.split('.')[-1] == 'db':
            datenbanken.append(i)
    for index, datenbank in enumerate(datenbanken):
        print(index, datenbank)


def turnier_auslosung(datenbank_name):
    conn = sqlite3.connect(datenbank_name + ".db")
    c = conn.cursor()
    c.execute(""" SELECT Team_ID FROM Teilnehmer """)
    teilnehmer = c.fetchall()
    anzahl = len(teilnehmer)
    print("Anzahl der Teilnehmer: " + str(anzahl))
    teilnehmer_liste = []
    if anzahl % 2 != 0:
        print("Es muss mit Freilos gespielt werden !")
        teilnehmer_liste.append(0)
    for i in teilnehmer:
        teilnehmer_liste.append(i[0])
    random.shuffle(teilnehmer_liste)
    teilnehmer_liste2 = []
    for i in range(len(teilnehmer_liste) // 2):
        a = teilnehmer_liste.pop()
        teilnehmer_liste2.append(a)
    print(teilnehmer_liste, teilnehmer_liste2)
    counter = 0
    for i in range(len(teilnehmer_liste)):
        c.execute("""INSERT into Spielablauf (Spiel_ID, Runde, Gegner_1, Gegner_2) Values(?, 1, ?, ?)""",
                  (100 + counter, teilnehmer_liste[counter], teilnehmer_liste2[counter]))
        conn.commit()
        counter += 1
    c.execute("SELECT * FROM Spielablauf")
    test = c.fetchall()
    print(test)
    conn.close()

# class Teilnehmer():
#     def __init__ (self, startnummer, teamname, aktiv, freilos):
#         self.startnummer = startnummer
#         self.teamname = teamname
#         self.aktiv = aktiv
#         self.freilos = freilos
#
#     def get_eigenschaften(self):
#         return self.startnummer + "," + self.teamname + "," + self.aktiv + "," + self.freilos
