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
aufruf = ""
num = 0
de_bit = 0
en_bit = 0
ges_bit = 0


def db_select(aufruf):
    inhalt = ""
    c.execute(aufruf)
    inhalt = c.fetchall()
    print(inhalt)
    # print(counter_aufruf)
    return inhalt


def aufrufe():
    ii = 0
    c.execute("SELECT * FROM Aufrufe")
    counter = c.fetchall()
    (ii) = counter[0][0]
    ii += 1
    print("ii: ",ii, "counter: ",counter)
    c.execute("UPDATE Aufrufe SET Anzahl=?", (ii,))
    conn.commit()
    return ii


def deutsch_englisch(deutsch, englisch, de_bit, en_bit, ges_bit):
    print("Was heißt ", deutsch, " auf Englisch?")
    eingabe = input("Deine Antwort lautet: ")
    ende_abfrage(eingabe)
    if eingabe == englisch:
        print("Richtig")
        de_bit = 1
    if en_bit == 1:  #todo klären
        ges_bit *= 2
    else:
        print("Falsche Antwort")
    print("D-E: ", de_bit, en_bit, ges_bit)
    return de_bit, en_bit, ges_bit

def englisch_deutsch(deutsch, englisch, de_bit, en_bit, ges_bit):
    print("Was heißt ", englisch, " auf Deutsch?")
    eingabe = input("Deine Antwort lautet: ")
    ende_abfrage(eingabe)
    if eingabe == deutsch:
        print("Richtig")
        en_bit = 1
        if de_bit == 1:
            ges_bit *= 2
    else:
        print("Falsche Antwort")
    print("E-D: ", de_bit, en_bit, ges_bit)
    return de_bit, en_bit, ges_bit

def db_update(aufruf):
    print(num)
    c.execute("UPDATE Deutsch_Englisch SET DE_bit=?, EN_bit=?, Ges_bit=? WHERE Num=? ", (de_bit, en_bit, ges_bit, num))
    # c.execute(aufruf)
    conn.commit()

def sort(inhalt):
    gr_begriffe = []
    gr_begriffe = inhalt
    random.shuffle(gr_begriffe)
    print("Gruppe-Fehler: ", gr_begriffe)
    return gr_begriffe

def ende_abfrage(eingabe):
    eingabe1 = eingabe.lower()
    if eingabe1 == "quit":
        print("Programm beenden")
        exit()


aufruf = ("SELECT * FROM Deutsch_Englisch")
# Inhalt string aus DB
inhalt = db_select(aufruf)
gr_begriffe = sort(inhalt)
ii= aufrufe()

for i in gr_begriffe:
    print(i)
    num, deutsch, englisch, de_bit, en_bit, ges_bit = i
    # print(num, deutsch, englisch, de_bit, en_bit, ges_code)
    if de_bit == 0:
        #deutsch_englisch(i, de_bit, en_bit, ges_bit)
        de_bit, en_bit, ges_bit = deutsch_englisch(deutsch, englisch, de_bit, en_bit, ges_bit)
        print(de_bit, en_bit, ges_bit)
    elif en_bit == 0:
        de_bit, en_bit, ges_bit = englisch_deutsch(deutsch, englisch, de_bit, en_bit, ges_bit)
        #(i, de_bit, en_bit, ges_bit) = englisch-deutsch()
        print(i)
    elif ii > ges_bit:
        de_bit = 0
        en_bit = 0
    print("update: ", de_bit, en_bit, ges_bit, num)
    aufruf = ("UPDATE Deutsch_Englisch SET DE_bit=?, EN_bit=?, Ges_bit=? WHERE Num=? ", (de_bit, en_bit, ges_bit, num))
    db_update(aufruf)
    time.sleep(5)