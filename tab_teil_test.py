import sqlite3

team1 = 1
conn = sqlite3.connect("8erTeam.db")
c = conn.cursor()
et01 = 13
et02 = 5
c.execute("SELECT * FROM Teilnehmer WHERE Team_ID=?", (team1,))
rows = c.fetchall()
print(rows)
#[t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19]=c.fetchall()
g_Diff_Pu       = 0
ho1_Pu_Diff     = 0
ho2_Pu_Diff     = 0
ho3_Pu_Diff     = 0
counter         = 100

if et01 > et02:
    gSpiele1 = rows[0][4] +1
    g_Diff_Pu= (et01 + -et02) + rows[0][5]
    if (et01 - et02) >= rows[0][6]:
        ho3_Pu_Diff = rows[0][7]
        ho2_Pu_Diff = rows[0][6]
        ho1_Pu_Diff = et01 - et02
        print(gSpiele1, ho1_Pu_Diff)
    elif () >= ho2_Pu_Diff:
        ho3_Pu_Diff = rows[0][7]
        ho2_Pu_Diff = rows[0][6]
    elif rows[0][6] >= ho3_Pu_Diff:
        ho3_Pu_Diff = rows[0][7]

    if counter[0:1] == 1
        Runde1= et01 - et02
c.execute("UPDATE Teilnehmer SET gew_Spiele=?, G_Diff_Punkte=?, H1_Pu_Diff=?, H2_Pu_Diff=?, H3_Pu_Diff=? WHERE Team_ID=?", (gSpiele1, g_Diff_Pu, ho1_Pu_Diff,ho2_Pu_Diff,ho3_Pu_Diff,team1))
conn.commit()
"""
    et011 = et01 - et02
    et022 = et02 - et01
    print(gSpiele1, " ", g_Diff_Pu)
else:
    gSpiele1 = 0
    gSpiele2 = 1
    et011 = et02 - et01
    et022 = et01 - et02
"""