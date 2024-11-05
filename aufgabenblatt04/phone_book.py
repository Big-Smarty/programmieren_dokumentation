from dataclasses import dataclass
import os.path


@dataclass(unsafe_hash=True)
class Entry:
    name: str
    number: str


entries = []
if os.path.isfile("book.db"):
    book = open("book.db", "r")
else:
    book = open("book.db", "x")

for e in book:
    e = e.split("$")
    entries.append(Entry(e[0], e[1]))
book.close()

action = int(
    input(
        "Soll ein neuer Eintrag gemacht werden (1) oder nach einer Telefonnummer gesucht werden (2)?\n"
    )
)
match action:
    case 1:
        entries.append(Entry(input("Name: \n"), input("Nummer: \n")))
    case 2:
        fragment = input("Name:\n")
        candidates = []
        for e in entries:
            if fragment.lower() in e.name.lower():
                candidates.append(e)
        if candidates == []:
            print("Es konnten keine passenden Einträge gefunden werden!")
        for c in candidates:
            print("Name: " + c.name + "\n" + "Nummer: " + c.number + "\n\n")

book = open("book.db", "w")
book.writelines(f"{e.name}${e.number}\n" for e in list(set(entries)))

book.close()
