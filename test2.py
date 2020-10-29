
import random

starter_liste = ["Dieter", "Uwe", "Julius", "Andy", "FRank", "Michael", "Kurt", "Ralf"]

los_trommel1= []
los_trommel2= []
counter = 0

random.shuffle(starter_liste)
print(starter_liste)
counter1 = len(starter_liste)
print(counter)
while counter < len(starter_liste):
    if counter <= (counter1 // 2) -1:
        los_trommel1.append(starter_liste[counter])
    else:
        los_trommel2.append(starter_liste[counter])
    counter += 1
print(los_trommel1)
print(los_trommel2)
counter = 0
print(f"{'Team 1':8s} {' ':13} {'Team 2':8s}")
while counter < len(los_trommel2):
    team10= los_trommel1[counter]
    team11= los_trommel2[counter]
    team20= los_trommel1[counter +1]
    team21= los_trommel2[counter +1]
    print(f"{team10:7s} {', ':2} {team11:7s} {' - '} {team20:7s} {', '} {team21:7s}")
    #print(los_trommel1[counter], ", ", los_trommel2[counter]," - ", los_trommel1[counter +1], ", ", los_trommel2[counter +1])
    counter +=2