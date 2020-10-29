import sqlite3

ru01 = ru02 = ru03 = ru04 = ru05 = ru01_ge= ru02_ge = ru03_ge = ru04_ge = ru05_ge = 0



class Tabelle:
    def teilnehmer_sel(team):
        global rows
        c.execute("SELECT * FROM Teilnehmer WHERE Team_ID=?", (team,))
        rows = c.fetchall()

    def teilnehmer_up(gSpiele1, et011, ho1_Pu_Diff, ho2_Pu_Diff, ho3_Pu_Diff, ru01, ru02, ru03, ru04, ru05, ru01_ge, ru02_ge, ru03_ge, ru04_ge, ru05_ge, team1):
        c.execute(
            "UPDATE Teilnehmer SET gew_Spiele= gew_Spiele + ?, G_Diff_Punkte= G_Diff_Punkte + ?, H1_Pu_Diff=?, H2_Pu_Diff=?, H3_Pu_Diff=?, Runde1=?, Runde2=?, Runde3=?, Runde4=?,Runde5=?, Ru1_Ge=?, Ru2_Ge=?, Ru3_Ge=?, Ru4_Ge=?, Ru5_Ge=? WHERE Team_ID=?",
            (gSpiele1, et011, ho1_Pu_Diff, ho2_Pu_Diff, ho3_Pu_Diff, ru01, ru02, ru03, ru04, ru05, ru01_ge, ru02_ge, ru03_ge, ru04_ge, ru05_ge, team1))
        conn.commit()

    def spielablauf_sel():
        global rows
        c.execute("SELECT * FROM Spielablauf WHERE Spiel_ID=?", (ruNu,))
        rows = c.fetchall()
    def spielablauf_up():
        c.execute("UPDATE Spielablauf SET  Punkte_G1=?, Punkte_G2=? WHERE Spiel_ID=?", (et01, et02, ruNu))
        conn.commit()

    def ergebnis(team, gSpiele, et, team_ge):
        global ru01, ru02, ru03, ru04, ru05, ru01_ge, ru02_ge, ru03_ge, ru04_ge, ru05_ge
        Tabelle.teilnehmer_sel(team)
        print(team, " ", rows)
        if et >= rows[0][6]:
            ho3_Pu_Diff = rows[0][7]
            ho2_Pu_Diff = rows[0][6]
            ho1_Pu_Diff = et
        elif et >= rows[0][7]:
            ho3_Pu_Diff = rows[0][7]
            ho2_Pu_Diff = et
            ho1_Pu_Diff = rows[0][6]
        elif et >= rows[0][8]:
            ho3_Pu_Diff = et
            ho2_Pu_Diff = rows[0][7]
            ho1_Pu_Diff = rows[0][6]
        else:
            ho3_Pu_Diff = rows[0][8]
            ho2_Pu_Diff = rows[0][7]
            ho1_Pu_Diff = rows[0][6]

        if ruNu1 == 1:
            ru01 = et
            ru01_ge = team_ge
            print(ru01_ge)
        if ruNu1 == 2:
            ru01 = rows[0][9]
            ru02 = et
            ru01_ge = rows[0][14]
            ru02_ge = team_ge
        print(ho1_Pu_Diff)
        Tabelle.teilnehmer_up(gSpiele, et, ho1_Pu_Diff, ho2_Pu_Diff, ho3_Pu_Diff, ru01, ru02, ru03, ru04, ru05, ru01_ge,
                              ru02_ge, ru03_ge, ru04_ge, ru05_ge, team)
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
        rows = c.fetchall()
        print(rows)
        for i in range(len(rows)):
            if i < len(rows):
                print(rows[i][0], "  ", rows[i][1], " : ", rows[i][2])
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
            Tabelle.spielablauf_up()
            Tabelle.spielablauf_sel()
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
        Tabelle.ergebnis(team1, gSpiele1, et011, team2)
        Tabelle.ergebnis(team2, gSpiele2, et022, team1)
