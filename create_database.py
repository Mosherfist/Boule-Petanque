import os
import sqlite3


def datenbank_erstellen(datenbank_name: object) -> object:
    if os.path.exists(datenbank_name + ".db"):
        print("Datenbank bereits vorhanden ! Bitte neuen Namen wählen")
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
        print("Datenbank " + datenbank_name + ".db" + "und Tabellen erfolgreich erstellt")


datenbank_erstellen("Boule")
