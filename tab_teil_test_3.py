import sqlite3

class Tabelle:
    def teilnehmer_sel(team):
        global rows
        c.execute("SELECT * FROM Teilnehmer WHERE Team_ID=?", (team,))
        rows = c.fetchall()

def FeEinGabe(eingabe01):
    #global eingabe01
    print("Fehlerhafte Eingabe!!!", eingabe01)
    eingabe01 = "falsch"

conn = sqlite3.connect("8erTeam.db")
c = conn.cursor()
eingabe = ""



while (eingabe != "quit"):
    if eingabe != "quit":
        c.execute("SELECT Spiel_ID, Gegner_1, Gegner_2 FROM Spielablauf WHERE Punkte_G1 IS 0 AND Punkte_G2 IS 0")
        conn.commit()
        inhalt = c.fetchall()
        print(inhalt)
        for i in range(len(inhalt)):
            if i < len(inhalt):
                print(inhalt[i][0], "  ", inhalt[i][1], " : ", inhalt[i][2])
                i += 1
        print("\nSpielergebnisse wie folgt eintragen: lfd-Ergebnis1:Ergebnis2 \n\
              Spielrunden.p: 101-13:00\n\
              oder Quit für Beenden")
        eingabe = input("Deine Eingabe:")
        eingabe01 = eingabe.lower()
        if eingabe01 != "quit":
            try:
                ruNu = int(eingabe[0:3])                        # Spiel_ID
                et01 = int(eingabe[4:6])                        # 1. Spielergebnis
                et02 = int(eingabe[7:9])                        # 2. Spielergebnis
                ruNu1=int(eingabe[0:1])
            except:
                FeEinGabe(eingabe01)
                ergebnisse()
            if (et01 > 13) or (et02 > 13) or (et01 == et02):
                FeEinGabe(eingabe01)
                ergebnisse()
                #except ValueError:
                #FeEinGabe()
            c.execute("UPDATE Spielablauf SET  Punkte_G1=?, Punkte_G2=? WHERE Spiel_ID=?", (et01, et02, ruNu))
            conn.commit()
            c.execute("SELECT * FROM Spielablauf WHERE Spiel_ID=?", (ruNu,))
            rows = c.fetchall()
            team1 = rows[0][2]
            team2 = rows[0][3]
            if et01 > et02:
                gSpiele1 = 1
                gSpiele2 = 0
                et011 = et01 - et02
                et022 = et02 + -et01
                print(et011, et022)
            else:
                gSpiele1 = 0
                gSpiele2 = 1
                et022 = et02 - et01
                et011 = et01 - et02
#TODO: Offene Spiele anzeigen

            #c.execute("SELECT * FROM Teilnehmer WHERE Team_ID=?", (team1,))
            #rows = c.fetchall()
            if ruNu1 == 1:
                c.execute("UPDATE Teilnehmer SET gew_Spiele=?, G_Diff_Punkte=?, H1_Pu_Diff=?, Runde1=?, Ru1_Ge=?  WHERE Team_ID=?",
                (gSpiele1, et011, et011, et011, team2, team1))
                c.execute("UPDATE Teilnehmer SET gew_Spiele=?, G_Diff_Punkte=?, H1_Pu_Diff=?, Runde1=?, Ru1_Ge=?  WHERE Team_ID=?",
                (gSpiele2, et022, et022, et022, team1, team2))
                conn.commit()
            if ruNu1 > 1:                   #Abfrage für Team1
                #c.execute("SELECT * FROM Teilnehmer WHERE Team_ID=?", (team1,))
                #rows = c.fetchall()
                Tabelle.teilnehmer_sel(team1)
                print(team1, " ", rows)
                if et011 >= rows[0][6]:
                    ho3_Pu_Diff = rows[0][7]
                    ho2_Pu_Diff = rows[0][6]
                    ho1_Pu_Diff = et011
                elif et011 >= rows[0][7]:
                    ho3_Pu_Diff = rows[0][7]
                    ho2_Pu_Diff = et011
                    ho1_Pu_Diff = rows[0][6]
                elif et011 >= rows[0][8]:
                    ho3_Pu_Diff = et011
                    ho2_Pu_Diff = rows[0][7]
                    ho1_Pu_Diff = rows[0][6]
                if ruNu1 == 2:
                    c.execute(
                        "UPDATE Teilnehmer SET gew_Spiele= gew_Spiele + ?, G_Diff_Punkte= G_Diff_Punkte + ?, H1_Pu_Diff=?, H2_Pu_Diff=?, H3_Pu_Diff=?, Runde2=?, Ru2_Ge=?  WHERE Team_ID=?",
                        (gSpiele1, et011, ho1_Pu_Diff, ho2_Pu_Diff, ho3_Pu_Diff,et011, team2, team1))

                if ruNu1 > 1:           #Abfrage für Team2
                    #c.execute("SELECT * FROM Teilnehmer WHERE Team_ID=?", (team2,))
                    #rows = c.fetchall() 
                    Tabelle.teilnehmer_sel(team2)
                    print(team2," ", rows)
                    if et022 >= rows[0][6]:
                        ho3_Pu_Diff = rows[0][7]
                        ho2_Pu_Diff = rows[0][6]
                        ho1_Pu_Diff = et022
                    elif et022 >= rows[0][7]:
                        ho3_Pu_Diff = rows[0][7]
                        ho2_Pu_Diff = et022
                        ho1_Pu_Diff = rows[0][6]
                    elif et022 >= rows[0][8]:
                        ho3_Pu_Diff = et022
                        ho2_Pu_Diff = rows[0][7]
                        ho1_Pu_Diff = rows[0][6]
                    if ruNu1 == 2:
                        c.execute(
                            "UPDATE Teilnehmer SET gew_Spiele= gew_Spiele + ?, G_Diff_Punkte= G_Diff_Punkte + ?, H1_Pu_Diff=?, H2_Pu_Diff=?, H3_Pu_Diff=?, Runde2=?, Ru2_Ge=?  WHERE Team_ID=?",
                            (gSpiele2, et022, ho1_Pu_Diff, ho2_Pu_Diff, ho3_Pu_Diff, et022, team1, team2))
                conn.commit()
conn.close()