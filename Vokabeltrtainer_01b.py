"""
Dieser Vokabeltrainer Deutsch-Englisch, Englisch-Deutsch funtiniert wie folgt:
> Dieser besteht aus einer Datenbank mit 2 Tabellen
>>  Anzahl der Aufrufe - Nach jedem Pgm-Start wird der Zähler um 1 erhöht.
>> Bereitgestellte Begriffe
> Alle Begriffe werden aus einer SQL-Datenban eingelesen
> Die eingelesen DB-Einträge werden gemischt (random)
> Danach erfolgt eine Abfrage der Begriffe zuerst Deutsch-Englisch. Ist der eingebenen Begriff richtig, wird ein Bit gesetzt.
> Danach erfolgt eine Abfrage der Begriffe Englisch-Deutsch. Ist der eingebenen Begriff richtig, wird ein Bit gesetzt.
> Wurde für ein Begriff 2x ein Bit gesetzt, wird das Ges-Bit um 1 erhöht und mal 2 potenziert.
> ist der Aufruf-Zähler höher als Ges-Zähler, werden die Bits für Deutsch-Englisch und Englisch-Deutsch wirder auf 0 gesetzt.- so kann es vorkommen
dass der Begriff nochmals als Ab frage erscheint.
"""

import sqlite3, random, time

    # Liste mit Begriffen aus der Datenbank
gr_begriffe = []

conn = sqlite3.connect("Vokabeltrainer.db")
c = conn.cursor()
aufruf= ""
num= 0
#counter= 0


def db_select(aufruf):
    inhalt=""
    # Pgm Aufruf-Zähler aus der Datenbank
    #counter_aufruf = 0
    c.execute(aufruf)
    inhalt = c.fetchall()
    print(inhalt)
    #print(counter_aufruf)
    aufrufe()
    return inhalt

def aufrufe():
    global ii  ###klären
    c.execute("SELECT * FROM Aufrufe")
    counter = c.fetchall()
    print(counter)
    (ii)=counter[0][0]
    print(ii)
    ii +=1
    print(ii)
    c.execute("UPDATE Aufrufe SET Anzahl=?", (ii,))
    conn.commit()
    #return ii




def db_update(aufruf):
    print(num)
    c.execute("UPDATE Deutsch_Englisch SET DE_bit=?, EN_bit=?, Ges_bit=? WHERE Num=? ", (de_bit, en_bit,ges_bit, num))
    #c.execute(aufruf)
    conn.commit()

def sort(inhalt):
    gr_begriffe = []
    gr_begriffe= inhalt
    random.shuffle(gr_begriffe)
    print("Gruppe-Fehler: ",gr_begriffe)
    return gr_begriffe
    #return inhalt

def ende_abfrage(eingabe):
    eingabe1=eingabe.lower()
    if eingabe1 == "quit":
        print("Programm beenden")
        exit()

aufruf=("SELECT * FROM Deutsch_Englisch")
#Inhalt string aus DB
inhalt= db_select(aufruf)
gr_begriffe=sort(inhalt)
for i in gr_begriffe:
    print(i)
    (num, deutsch, englisch, de_bit, en_bit, ges_bit) =i
    #print(num, deutsch, englisch, de_bit, en_bit, ges_code)
    if en_bit ==0:
        print("Was heißt ",deutsch," auf Englisch?")
        eingabe=input("Deine Antwort lautet: ")
        ende_abfrage(eingabe)
        if eingabe == englisch:
            print("Richtig")
            en_bit= 1
            if de_bit== 1:
                ges_bit  **=2
            #aufruf=("UPDATE Deutsch_Englisch SET EN_r_f='r' WHERE Num= 1")
            #aufruf=("UPDATE Deutsch_Englisch SET DE_bit=?, EN_bit=?, Ges_r_f=? WHERE Num=? ", (de_bit, en_bit,ges_code, num))
            #db_update(aufruf)
        else:
            print("Falsche Antwort")

    elif de_bit == 0:
        print("Was heißt ", englisch, " auf Deutsch?")
        eingabe = input("Deine Antwort lautet: ")
        ende_abfrage(eingabe)
        if eingabe == deutsch:
            print("Richtig")
            de_code = 1
            if en_code == 1:
                ges_code **=2
            # aufruf=("UPDATE Deutsch_Englisch SET EN_r_f='r' WHERE Num= 1")
            #aufruf=("UPDATE Deutsch_Englisch SET DE_bit=?, EN_bit=?, Ges_r_f=? WHERE Num=? ",(de_code, en_code, ges_code, num))
            #db_update(aufruf)
        else:
            print("Falsche Antwort")

    aufruf=("UPDATE Deutsch_Englisch SET DE_bit=?, EN_bit=?, Ges_bit=? WHERE Num=? ", (de_bit, en_bit,ges_bit, num))
    db_update(aufruf)
    print("Counter: ",ii)

    time.sleep(5)




#aufruf=("SELECT * FROM Deutsch_Englisch WHERE Num= ")
#db_abfrage(aufruf)



"""
do while input == "quit":
    if input != "quit":
        aufruf = "SELECT Team_ID FROM Teilnehmer WHERE Aktiv = 'A' "
        db.(aufruf)



def db_abfrage():
    c.execute("SELECT * FROM Spielablauf")
    conn.commit()
    inhalt_sp = c.fetchall()
    print(inhalt_sp)
"""






"""
do while input == "quit":
    if input != "quit":
        aufruf = "SELECT Team_ID FROM Teilnehmer WHERE Aktiv = 'A' "
        db.(aufruf)
"""