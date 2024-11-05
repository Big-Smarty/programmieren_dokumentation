from datetime import date
from typing import List
import os


class Person:
    def __init__(self, nachname, vorname, geburtsdatum):
        self._nachname: str = nachname
        self._vorname: str = vorname
        self._geburtsdatum: date = geburtsdatum

    def __str__(self):
        return f"{self.vorname} {self.nachname}, {self.geburtsdatum}"

    @property
    def nachname(self):
        return self._nachname

    @property
    def vorname(self):
        return self._vorname

    @property
    def geburtsdatum(self):
        return self._geburtsdatum


class Personendatenbank:
    def __init__(self, personen):
        self._personen: List[Person] = personen

    def leeren(self):
        self._personen = []

    def einfügen(self, person):
        self._personen.append(person)

    def lade(self, datei):
        self._personen = []
        for l in datei.readlines():
            temp = l.split("$")
            self._personen.append(Person(temp[0], temp[1], temp[2]))

    def speichere(self, datei):
        for p in self.personen:
            datei.write(f"{p.nachname}${p.vorname}${p.geburtsdatum}$\n")

    def findePerson(self, name, vorname):
        for p in self.personen:
            if p.nachname.lower() == name.lower():
                if p.vorname.lower() == vorname.lower():
                    return p
        return None

    @property
    def personen(self):
        return self._personen


pdb = Personendatenbank([])

while True:
    action = int(
        input(
            """
        Guten Tag. Hier können sie ihre Mitarbeiter/Klienten/Sonstiges verwalten. Wählen sie eine Aktion aus!
        0 => Programm verlassen
        1 => Datenbank leeren
        2 => Person einfügen
        3 => Datenbank aus Datei laden
        4 => Datenbank in Datei speichern
        5 => Person finden
        """
        )
    )
    match action:
        case 0:
            break
        case 1:
            pdb.leeren()
            continue
        case 2:
            name = input("Nachname: \n")
            vorname = input("Vorname: \n")
            geburtsdatum = input("Geburtsdatum: \n")
            pdb.einfügen(Person(name, vorname, geburtsdatum))
            continue
        case 3:
            pfad = input("Welche Datei wollen sie laden?\n")
            if not os.path.isfile(pfad):
                print("Tut uns leid, diese Datei existiert nicht.\n")
                continue
            dbfile = open(pfad, "r")
            pdb.lade(dbfile)
            continue
        case 4:
            pfad = input("Wie soll die Datei heißen?\n")
            dbfile = open(pfad, "w")
            pdb.speichere(dbfile)
            continue
        case 5:
            name = input("Wie heißt ihre Person zum Nachnamen?\n")
            vorname = input("Und zum Vornamen?\n")
            person = pdb.findePerson(name, vorname)
            if person == None:
                print(
                    "Tut uns leid, diese Person existiert nicht in unserer Datenbank."
                )
                continue
            print(person.__str__())
            continue
