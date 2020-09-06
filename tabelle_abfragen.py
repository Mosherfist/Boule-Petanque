import sqlite3

def tabelle_abfragen(datenbank_name):
    stand = []
    conn = sqlite3.connect(datenbank_name + ".db")
    c = conn.cursor()
    c.execute(""" SELECT Name,  gewonnene_Spiele, Punkte FROM Teilnehmer ORDER by Punkte DESC """)
    tabelle = c.fetchall()
    for i in tabelle:
        Name, gewonnene_Spiele, Punkte = i
        print(Name, gewonnene_Spiele, Punkte)
        stand.append(Name, gewonnene_Spiele, Punkte)
    return stand
    conn.close()
