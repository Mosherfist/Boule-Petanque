import os, sys, sqlite3,glob, random
#Kommentar

def datenbank_erstellen(db_name):
    if os.path.exists(db_name + ".db"):
        print("Datenbank bereits vorhanden ! Bitte neuen Namen wählen")
    else:
        print("Erstelle neue Turnierdatenbank und die zugehörigen Tabellen...")
        conn = sqlite3.connect(db_name + ".db")
        c = conn.cursor()
        #c.execute("CREATE TABLE Teilnehmer (Team_ID INTEGER Primary Key, Teamname TEXT, Aktiv TEXT, Freilos TEXT, gew_Spiele INTEGER, Diff_Punkte INTEGER)")
        sql_anweisung = """
        CREATE TABLE Teilnehmer (
        Team_ID INTEGER Primary Key, 
        Teamname TEXT, 
        Aktiv TEXT, 
        Freilos TEXT, 
        gew_Spiele INTEGER, 
        G_Diff_Punkte INTEGER,
        H1_Pu_Diff INTEGER,
        H2_Pu_Diff INTEGER,
        H3_Pu_Diff INTEGER,
        Runde1 INTEGER,
        Runde2 INTEGER,
        Runde3 INTEGER,
        Runde4 INTEGER,
        Runde5 INTEGER,
        Ru1_Ge INTEGER,
        Ru2_Ge INTEGER,
        Ru3_Ge INTEGER,
        Ru4_Ge INTEGER,
        Ru5_Ge INTEGER
        );"""
        c.execute(sql_anweisung)
        c.execute(" CREATE TABLE Spielablauf (Spiel_ID INTEGER PRIMARY KEY, Runde INTEGER, Gegner_1 INTEGER, Gegner_2 INTEGER, Gewinner INTEGER, Punkte_G1 INTEGER, Punkte_G2 INTEGER, Status Text)")
        conn.commit()
        conn.close()
        print("Datenbank " + db_name + ".db" + " und Tabellen erfolgreich erstellt")


file_db = []
count   = 0
def datenbanken_auflisten():
    global count
    for file in glob.glob("*.db"):
        file_db.append(file)
        count += 1
        print(count, "  ",file)

def anz_bahnen():
    pass
#TODO: Anzahl Bahnen erfassen und betreuen
"""
> Anzahl Bahnen (Spielfelder) und TL (Terra Libre) erfassen
> Jede Spielbahn kann zu jeder Zeit gesperrt bzw. freigegeben werden.
>> Oftmals will man bei Endspielen, ganz bestimmte Bahnen haben, damit die Zuschauer auch etwas davon haben.
>> Terra Libre = Die Teams müssen sich ihre Spielmöglichkeiten selbst suchen. Diese Möglichkeit wird genutz, wenn die Anzahl der Bahnen nicht ausreicht.
>> Anzahl der Bahnen und evtl TL einmalig erfassen und speichern.
>> Bei weiteren Turnieren wird lediglich abgefragt, ob gespeicherten Daten noch richtig sind.
>> Es gibt weniger Bahnen (kein TL), als Spielpaarungen:
>>> Nach einer beendeten Spielpaarung wird das nächste Team auf der frei gewordenen Bahn eingesetzt.
>> Es gibt mehr Bahnen als Spielpaarungen in einer Runde:
>>> Hier wird darauf geachtet, dass alle Bahnen in etwa die gleiche Anzahl von Spielpaarungen hat.
"""


def tn_erfassen():
    eingabe1_tn = ""
    print(db_name)
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    while eingabe1_tn != "quit":
        print("\n\
                         Naechstes Team eingeben, oder            \n\
                         Quit  Beenden  ")
        eingabe_tn = input("Deine Eingabe: ")
        eingabe1_tn = eingabe_tn.lower()
        if eingabe1_tn != "quit":
            #c.execute("INSERT INTO Teilnehmer(Teamname,Aktiv, Freilos,gew_Spiele, Diff_Punkte) VALUES (?,?,?,?,?)",
             #         (eingabe_tn[:20], 'A','N',0,0))
            c.execute("INSERT INTO Teilnehmer(Teamname, Aktiv, Freilos, gew_Spiele, G_Diff_Punkte, H1_Pu_Diff, H2_Pu_Diff, H3_Pu_Diff,Runde1, Runde2, Runde3, Runde4, Runde5, Ru1_Ge, Ru2_Ge, Ru3_Ge, Ru4_Ge, Ru5_Ge) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(eingabe_tn[:20], 'A', 'N', 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0))
            #c.execute("INSERT INTO Teilnehmer VALUES (Teamname, Aktiv, Freilos)", (eingabe_tn[:20], 'A', 'N'))
            conn.commit()
            c.execute("SELECT * FROM Teilnehmer ORDER BY team_ID DESC LIMIT 1")
            rows = c.fetchall()
            print(type(rows))
            print(rows)
            print("Startnummer: ", rows[0][0], " Team: ", rows[0][1])
        else:
            conn.close()


def tn_Aktiv(flag):
    eingabe1_tn = ""
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    while eingabe1_tn != "quit":
        print("\n\
                            Welches Team soll inaktiv gesetzt werden?           \n\
                            Startnummer eingeben                                \n\
                            Quit  Beenden  ")
        eingabe_tn = input("Deine Eingabe: ")
        eingabe1_tn = eingabe_tn.lower()
        if eingabe1_tn != "quit":
            print(db_name, eingabe_tn, flag)
            c.execute("UPDATE Teilnehmer SET Aktiv=? WHERE Team_id=?", (flag, eingabe_tn))
            conn.commit()
        else:
            conn.close()
##
##  Teilnehmerliste erstellen
##
def teilnehmerliste():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("""SELECT Team_ID, Teamname FROM Teilnehmer """)
    teilnehmer = c.fetchall()
    conn.close()
    print("Start#", "   ", "Teamname")
    for i in teilnehmer:
        team_ID, teamname = i
        print(f"{team_ID:6d} {'':3} {teamname:20s} ")
#TODO:  Teilnehmerliste in Flask ausgeben

def tn_tabelle():
    pass
#TODO: Teilnehmer Tabellestand in Flask erstellen
"""
> Wenn möglich, nach jeder Änderung automatisch aktualisieren
"""

def neue_runde():
    inhalt = []
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT * FROM Spielablauf")
    inhalt = c.fetchall()
    #print(inhalt)
    if not inhalt:                                                  ##Abfrage, ob Tabelle Spielablauf gefüllt
        turnier_auslosung()
    for i in range(len(inhalt)):
        #print(inhalt[i])
        if inhalt[i][5] or inhalt[i][6] == 0:
            print("\nEs fehlen noch Einträge der aktuellen Runde")
            ergebnisse()
            #i += 1
##Neue Runde noch offen################################################
#TODO: Neue Runde bearbeiten
"""
> Abfragen, ob alle Ergebnisse erfasst wurden. 
> Wenn ja:
>> Anhand einer neuen, aktuellen Tabelle werden die neuen Partien erstellt (Liste).
>>> Evtl. Paussierende dürfen nicht erfasst werden
>>> Teams mit Freilos müssen berücksichtigt werden
>>> Kein Team darf 2x gegeneinander spielen.
>> Hunderter Counter um 100 erhöhen 
> Wenn nein:
>> Print("Es müssen erst alle Ergebnisse erfasst sein")
>> Zurück zum Auswahl-Menue
"""
def turnier_auslosung():
    counter = 100
    los_trommel = []
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT Team_ID FROM Teilnehmer WHERE Aktiv = 'A' ")
    inhalt = c.fetchall()
    #print(inhalt[1])
    for db_satz in inhalt:
        #if db_satz[2) == "A":               ## Aktiv = Aktiv
        los_trommel.append(db_satz[(0)])
    print(los_trommel)
    random.shuffle(los_trommel)
    if len(los_trommel) % 2 != 0:
        los_trommel.append("F")
        print(los_trommel)
    while len(los_trommel):
        team1 = los_trommel.pop(0)
        team2 = los_trommel.pop(0)
        print(team1, " : ", team2)
        counter  +=1
        c.execute("INSERT INTO Spielablauf (Spiel_ID, Gegner_1, Gegner_2, Punkte_G1, Punkte_G2) VALUES (?,?,?,?,?)", (counter, team1, team2,0,0))
        conn.commit()
        if team2 == "F":
            c.execute("UPDATE Teilnehmer SET Freilos=? WHERE Team_ID=?", ("F", team1))
            conn.commit()
    conn.close()

def ergebnisse():
    eingabe = ""
    i = 0
    inhalt = []
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT Spiel_ID, Gegner_1, Gegner_2 FROM Spielablauf WHERE Punkte_G1 IS 0 ")
    #Achtung Punkte_G1 ist default 0!!!!
    conn.commit()
    inhalt = c.fetchall()
    #print(inhalt)
    for i in range(len(inhalt)):
        if i < len(inhalt):
            print(inhalt[i][0], "  ", inhalt[i][1], " : ", inhalt[i][2])
            i += 1
    while (eingabe != "quit"):
        if eingabe != "quit":
#TODO: Alle noch offenen Spiele anzeigen
            print("\nSpielergebnisse wie folgt eintragen: lfd-Ergebnis1:Ergebnis2 \n\
                  Spielrunden.p: 101-13:00\n\
                  oder Quit für Beenden")
            eingabe = input("Deine Eingabe:")
            eingabe01 = eingabe.lower()
            if eingabe01 != "quit":
                try:
                    ruNu = int(eingabe[0:3])
                    et01 = int(eingabe[4:6])
                    et02 = int(eingabe[7:9])
                except:
                    FeEinGabe(eingabe01)
                    ergebnisse()
                if (et01 > 13) or (et02 > 13) or (et01 == et02):
                    FeEinGabe(eingabe01)
                    ergebnisse()
                    #except ValueError:
                    #FeEinGabe()
                if et01 > et02:
                    gSpiele1 = 1
                    gSpiele2 = 0
                    et011 = et01 - et02
                    et022 = et02 - et01
                else:
                    gSpiele1 = 0
                    gSpiele2 = 1
                    et011 = et02 - et01
                    et022 = et01 - et02

                c.execute("UPDATE Spielablauf SET  Punkte_G1=?, Punkte_G2=? WHERE Spiel_ID=?", (et01, et02, ruNu))
                c.execute("SELECT * FROM Spielablauf WHERE Spiel_ID=?", (ruNu,))
                rows = c.fetchall()
                team1 = rows[0][2]
                team2 = rows[0][3]
                c.execute("UPDATE Teilnehmer SET Diff_Punkte= Diff_Punkte + ?, gew_Spiele= gew_Spiele + ? WHERE Team_ID=?", (et011, gSpiele1, team1))
                c.execute("UPDATE Teilnehmer SET Diff_Punkte= Diff_Punkte + ?, gew_Spiele= gew_Spiele + ? WHERE Team_ID=?", (et022, gSpiele2, team2))
                conn.commit()
                #print("Ergebnisse")
    conn.close()

def ergebnisse_korr():
    pass
#TODO: Ergebnisse korrigieren
"""
> Es werden alle eingetragenen Spiel-Ergebnisse aufgelistet
>> Der User kann nun eine Korrektur vornehmen
>>> Änderungen in Teilnehmer- und Spielablauf vornehmen
"""

def FeEinGabe(eingabe01):
    #global eingabe01
    print("Fehlerhafte Eingabe!!!", eingabe01)
    eingabe01 = "falsch"




db_name = ""
eingabe1 = ""
while eingabe1 != "quit":
    print("\n\
              Eine Auswahl treffen:                                    \n\
              Voreinstellunnen                                         \n\
              11    Turnier mit neuer Db-Tabelle starten                \n\
              12    Turnier mit bestehender Db-Tabelle starten           \n\
              13    Anzahl der Bahnen erfassen                            \n\
                                                                          \n\
              Teilnehmer                                                   \n\
              21    Teilnehmer erfassen                                    \n\
              22    Teilnehmer inaktiv setze                                \n\
              23    Teilnehmer aktiv setzen                                 \n\
              24    Teilnehmerliste anzeigen                                \n\
                                                                            \n\
              Spielrunden + Ergebnisse                                      \n\
              31    Neue Runde                                              \n\
              32    Ergebnisse eintragen                                    \n\
              33    Ergebnisse korrigieren                                  \n\
              34    Aktueller Tabellenstand anzeigen                         \n\
              Quit  Beenden  ")
    eingabe = input("\nDeine Eingabe: ")
    eingabe01 = eingabe.lower()
    if eingabe01 == "quit":
        sys.exit()
    if (eingabe != "11") and (eingabe != "12"):
        if db_name == "":
            print("Zuerst muss Punkt 11 oder 12 ausgewählt werden!!")
            break
            #TODO: SCHLEIFE abfangen und zum Auswahlmenu gelangen


    if eingabe == "11":
        print("Bitte neuen Datenbanknamen eingeben (Beispiel: Boule_Turnier)")
        db_name = input("Deine Eingabe: ")
        datenbank_erstellen(db_name)
        db_name= db_name + ".db"
        print(db_name)
    if eingabe == "12":
        datenbanken_auflisten()
        print("Tabellennummer eingeben: ")
        db_nummer= input("Deine Eingabe: ")
        db_name= file_db[int(db_nummer)-1]
        print(db_name)
    if eingabe == "13":
        print("Es wird noch daran gearbeitet")
        anz_bahnen()
    if eingabe == "21":
        tn_erfassen()
    if eingabe == "22":
        flag = 'P'
        tn_Aktiv(flag)
    if eingabe == "23":
        flag ="A"
        tn_Aktiv(flag)
    if eingabe == "24":
        teilnehmerliste()
    if eingabe == "31":
        neue_runde()
    if eingabe == "32":
        ergebnisse()
    if eingabe == "33":
        print("Es wird noch daran gearbeitet")
        ergebnisse_korr()
    if eingabe == "34":
        print("Es wird noch daran gearbeitet")
        tn_tabelle()
