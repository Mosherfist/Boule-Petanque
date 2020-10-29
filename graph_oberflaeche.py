##
##pythonbuch.com/gui.html
##

from tkinter import *
from datetime import date
print(date.today())


# Die folgende Funktion soll ausgeführt werden, wenn
# der Benutzer den Button anklickt
def button_action():
    anweisungs_label.config(text="Ich wurde geändert!")


# Ein Fenster erstellen und Größe definieren
fenster = Tk()
fenster.geometry("800x400")

# Den Fenstertitle erstellen
fenster.title("Vokabeltrainer Deutsch-Englisch - Englisch-Deutsch")

# Info_label erstellen
versions_label = Label(fenster,text="Version: 0.0.1")
#versions_label.place(relx = 0, rely= 0, width= 100, height= 50)
versions_label.grid(row = 0, column= 0, padx=10)

datums_label = Label(fenster, text="Datum: ")
#datums_label.place(relx = 100, rely= 500, width= 200, height= 150)
datums_label.grid(row = 0, column=1,padx=300)

# Label und Buttons erstellen.
#change_button = Button(fenster, text="Ändern", command=button_action)
#exit_button = Button(fenster, text="Beenden", command=fenster.quit)

#anweisungs_label = Label(fenster, text="Ich bin eine Anweisung:\n\
#Klicke auf 'Ändern'.")

#info_label = Label(fenster, text="Ich bin eine Info:\n\
#Der Beenden Button schliesst das Programm.")

# Nun fügen wir die Komponenten unserem Fenster
# in der gwünschten Reihenfolge hinzu.
#versions_label.pack()
#datums_label.pack()
#anweisungs_label.pack()
#change_button.pack()
#info_label.pack()
#exit_button.pack()

# In der Ereignisschleife auf Eingabe des Benutzers warten.
fenster.mainloop()