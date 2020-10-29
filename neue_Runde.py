import sqlite3, random, glob

inhalt_sp = []
inhalt_tn = []
los_trommel = []
counter = 100
conn = sqlite3.connect("8erTeam.db")
c = conn.cursor()
eingabe = ""

class db():
    def spielablauf(aufruf):
        global inhalt_sp
        c.execute(aufruf)
        conn.commit()
        inhalt_sp = c.fetchall()

    def teilnehmer(aufruf):
        global inhalt_tn
        c.execute(aufruf)
        conn.commit()
        inhalt_tn = c.fetchall()


def neue_runde():
    c.execute("SELECT * FROM Spielablauf")
    conn.commit()
    inhalt_sp = c.fetchall()
    print(inhalt_sp)

    #aufruf="SELECT TEAM_ID FROM (SELECT * FROM Teilnehmer ORDER BY gew_Spiele DESC, G_Diff_Punkte DESC, H1_Pu_Diff DESC, H2_Pu_Diff DESC) WHERE Aktiv = 'A' "
    #db.spielablauf(aufruf)
    c.execute("SELECT TEAM_ID FROM (SELECT * FROM Teilnehmer ORDER BY gew_Spiele DESC, G_Diff_Punkte DESC, H1_Pu_Diff DESC, H2_Pu_Diff DESC) WHERE Aktiv = 'A' " )
    conn.commit()
    inhalt_tn = c.fetchall()
    print(inhalt_tn)
##
## Abfrage nach Runde 01
##
    if not inhalt_sp:
        counter= 100
        turnier_auslosung(counter)

    for i in range(len(inhalt_sp)):             ## Sind alle Spielergebnisse eingetragen?
        print(inhalt_sp[i])
        print(inhalt_sp[i][5])
        if inhalt_sp[i][5] == 0 or inhalt_sp[i][6] == 0:
            print("\nEs fehlen noch Einträge der aktuellen Runde")
            #TODO noch offene Ergebnisse anzeigen
            #ergebnisse()
        neue_runde()
##
## Neue Spielrunde zusammen stellen
##
def turnier_auslosung(counter):
    los_trommel = []
    aufruf="SELECT Team_ID FROM Teilnehmer WHERE Aktiv = 'A' "
    db.teilnehmer(aufruf)
    print(inhalt_tn)
    for db_satz in inhalt_tn:
        los_trommel.append(db_satz[(0)])
    #print(los_trommel)
    random.shuffle(los_trommel)
    freilos(los_trommel)
    spielpaarungen(los_trommel)

def freilos(los_trommel):
    print("freilos: ", los_trommel)
    if len(los_trommel) % 2 != 0:
        los_trommel.append("F")

def spielpaarungen(los_trommel):
    global counter
    print("Spielpaarungen: ",los_trommel)
    while len(los_trommel):
        team1 = los_trommel.pop(0)
        team2 = los_trommel.pop(0)
        if str(team1) < str(team2):
            print(team1, " : ", team2)
        else:
            print(team2, " : ", team1)
        counter += 1
        c.execute("INSERT INTO Spielablauf (Spiel_ID, Gegner_1, Gegner_2, Punkte_G1, Punkte_G2) VALUES (?,?,?,?,?)",(counter, team1, team2, 0, 0))
        conn.commit()
##TODO: noch klären
        inhalt_sp = c.fetchall()
        #aufruf="INSERT INTO Spielablauf (Spiel_ID, Gegner_1, Gegner_2, Punkte_G1, Punkte_G2) VALUES (?,?,?,?,?)",(counter, team1, team2, 0, 0)
        #db.spielablauf(aufruf)




    #sp_paarungen()

#def sp_paarungen():




"""
        c.execute("SELECT TEAM_ID, Freilos, Runde1, Runde2, Runde3, Runde4, Runde5 FROM(SELECT * FROM Teilnehmer ORDER BY gew_Spiele DESC, G_Diff_Punkte DESC, H1_Pu_Diff DESC, H2_Pu_Diff DESC) WHERE Aktiv = 'A' ")
        inhalt = c.fetchall()
        print("inhalt: ", inhalt)
        for db_satz in inhalt:
            los_trommel.append(db_satz[(0)])
print("los_trommel: ",los_trommel)
##
## Abfrage nach ungerade Anzhal von Teams
##
if len(los_trommel) % 2 != 0:
    los_trommel.append("F")

##
## Abfrage hat Team bereits ein Freilos erhalten
##
    if inhalt[-1][1] == "N":
        print("alles ok")

    else:
        print("Team hatte schon ein Freilos")
        ## Nächstes Team abfragen
        ## Spielrunde neu mischen

    if team2 == "F":
        c.execute("UPDATE Teilnehmer SET Freilos=? WHERE Team_ID=?", ("F", team1))
        conn.commit()


    ## Bit Freilos in Teilnehmer-DB setzen
    ## Neue Runde anzeigen
    ## Counter hochsetzen (Beispiel: 201)
    ## Neue Runde in Spielablauf-DB eintragen

        #ergebnisse()
        #i += 1
##Neue Runde noch offen################################################
#TODO: Neue Runde bearbeiten
>> Anhand einer neuen, aktuellen Tabelle werden die neuen Partien erstellt (Liste).
>>> Evtl. Paussierende dürfen nicht erfasst werden
>>> Teams mit Freilos müssen berücksichtigt werden
>>> Kein Team darf 2x gegeneinander spielen.
>> Hunderter Counter um 100 erhöhen 
> Wenn nein:
>> Print("Es müssen erst alle Ergebnisse erfasst sein")
>> Zurück zum Auswahl-Menue


##Neue Runde noch offen################################################
#TODO: Neue Runde bearbeiten

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

def turnier_auslosung():
    counter = 100
    los_trommel = []
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT Team_ID FROM Teilnehmer WHERE Aktiv = 'A' ")
    inhalt = c.fetchall()
    print(inhalt)
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
"""
neue_runde()