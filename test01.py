import random

starter_liste = ["Dieter", "Uwe", "Julius", "Andy", "FRank", "Michael", "Kurt", "Ralf"]

los_trommel1= []
los_trommel2= []
counter = 0

random.shuffle(starter_liste)
print(starter_liste)
counter1 = len(starter_liste)
#print(counter)
while counter < len(starter_liste):
    if counter <= (counter1 // 2) -1:
        los_trommel1.append(starter_liste[counter])
    else:
        los_trommel2.append(starter_liste[counter])
    counter += 1
#print(los_trommel1)
#print(los_trommel2)
counter = 0
while counter < len(los_trommel1):
    print(los_trommel1[counter]," - ",los_trommel2[counter])
    counter += 1



"""
counter = 0

for i in range(0, len(starter_liste)):
    zwischenliste.append(i)

while counter < len(starter_liste) // 2:
    random.shuffle(zwischenliste)
    print(zwischenliste)
    #if zwischenliste not in zufallsliste or zwischenliste(reversed) not in zufallsliste:
    zufallsliste.append(zwischenliste)
    print(zufallsliste)
    counter += 1
"""