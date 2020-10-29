"""
Dieses Pgm soll ein Turnier mit 16 Teilnehmern zeigen.- Es spielen immer zwei Teams zusammen.
Jedes Team besteht aus 2 Teilnehmern.- Unabhängig vom Spielergebnis werden nach jeder Runde die Teams neu gemischt.
Dabei soll kein Team 2x in der gleichen Konstellation spielen.
Es werden 3 Runden gespielt.
"""
import random
#myListe=[1,2,3,4,5,6,7,8]

myListe=[]
liste1 = []
i    = 1
set3 = ""

def matches_out(liste, liste1):
    global set3
    set1 = set(liste)
    set2 = set(liste1)
    set3 = set1.intersection(set2)
    return len(set3)

myListe =list(range(1,17))


while i <= 3:
    kopie=list(myListe)
    random.shuffle(kopie)
    liste= []
    for j in range(len(kopie) //2):
        x=kopie.pop()
        y=kopie.pop()
        if x < y:
            liste.append((x,y))
        else:
            liste.append((y,x))
    matches_out(liste, liste1)
    if len(set3) < 1:
        liste1=list(liste)
        x=len(liste)
        n=0
        print("\nRunde ",i)
        i +=1
        while n < x:
            if str(n) < str(x):
                print(liste1[n]," - ",liste1[n+1])
                n +=2
            else:
                pass
    else:
        matches_out(liste, liste1)