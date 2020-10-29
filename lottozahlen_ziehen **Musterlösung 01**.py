#Dies ist meine modifizierte Lösung zum Thema "Lottozahlen ziehen":
import random

eingabe=""

def anfang():
    global eingabe
    print("Welches Lotto-System soll gespielt werden? \n\
        1.  Mittwoch-Lotto  (7 aus 64) \n\
        2.  Freitag-Lotto   (6 aus 50) \n\
        3.  Samstag-Lotto   (6 aus 49) ")
    eingabe = input("Deine Eingabe: ")

anfang()
if eingabe == "1":
    zahlen_ziehen=8
    ges_zahlen= 65
if eingabe == "2":
    zahlen_ziehen=7
    ges_zahlen=51
if eingabe == "3":
    zahlen_ziehen=7
    ges_zahlen=50


a= []
lottozahlen=[]
a=list(range(1,ges_zahlen))
random.shuffle(a)
#print(a)
lottozahlen=a[:zahlen_ziehen]
#print(lottozahlen)
zusatzzahl=lottozahlen.pop()
#print(zusatzzahl)
#lottozahlen.sort()
#print(lottozahlen)
print("Folgende Lotto-Zahlen würde ich tippen: ", sorted(lottozahlen), " Zusatzzahl: ", zusatzzahl)

