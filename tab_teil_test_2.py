import sqlite3


conn = sqlite3.connect("8erTeam.db")
c = conn.cursor()
eingabe = ""



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

            c.execute("SELECT * FROM Teilnehmer WHERE Team_ID=?", (team1,))
            rows = c.fetchall()
            if ruNu1 == 1:
                c.execute("UPDATE Teilnehmer SET gew_Spiele=?, G_Diff_Punkte=?, H1_Pu_Diff=?, Runde1=?, Ru1_Ge=?  WHERE Team_ID=?",
                (gSpiele1, et011, et011, et011, team2, team1))
                c.execute("UPDATE Teilnehmer SET gew_Spiele=?, G_Diff_Punkte=?, H1_Pu_Diff=?, Runde1=?, Ru1_Ge=?  WHERE Team_ID=?",
                (gSpiele2, et022, et022, et022, team1, team2))
                conn.commit()
                conn.close()
            if ruNu1 > 1:
                if et011 >= rows[0][6]:             #Höchste Pu_Differenz für Team1
                    ho13_Pu_Diff = rows[0][7]
                    ho12_Pu_Diff = rows[0][6]
                    ho11_Pu_Diff = et011


