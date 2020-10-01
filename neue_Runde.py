import sqlite3

inhalt = []
los_trommel = []
conn = sqlite3.connect("8erTeam.db")
c = conn.cursor()
eingabe = ""
#conn = sqlite3.connect(db_name)
#c = conn.cursor()
c.execute("SELECT * FROM Spielablauf")
inhalt = c.fetchall()
#print(inhalt)
#if not inhalt:                                                  ##Abfrage, ob Tabelle Spielablauf gefüllt
#    turnier_auslosung()
##
## Abfrage nach noch ausstehenden Ergebnissen
##
for i in range(len(inhalt)):
    #print(inhalt[i])
    if inhalt[i][5] == 0 and inhalt[i][6] == 0:
        print("\nEs fehlen noch Einträge der aktuellen Runde")
        pass
##
## Neue Spielrunde zusammen stellen
##
c.execute("SELECT TEAM_ID, Freilos FROM(SELECT * FROM Teilnehmer ORDER BY gew_Spiele DESC, G_Diff_Punkte DESC, H1_Pu_Diff DESC, H2_Pu_Diff DESC) WHERE Aktiv = 'A' ")
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

    ## Bit Freilos in Teilnehmer-DB setzen
    ## Neue Runde anzeigen
    ## Counter hochsetzen (Beispiel: 201)
    ## Neue Runde in Spielablauf-DB eintragen

        #ergebnisse()
        #i += 1
##Neue Runde noch offen################################################
#TODO: Neue Runde bearbeiten
"""
>> Anhand einer neuen, aktuellen Tabelle werden die neuen Partien erstellt (Liste).
>>> Evtl. Paussierende dürfen nicht erfasst werden
>>> Teams mit Freilos müssen berücksichtigt werden
>>> Kein Team darf 2x gegeneinander spielen.
>> Hunderter Counter um 100 erhöhen 
> Wenn nein:
>> Print("Es müssen erst alle Ergebnisse erfasst sein")
>> Zurück zum Auswahl-Menue
"""