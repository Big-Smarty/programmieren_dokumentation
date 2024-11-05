from dataclasses import dataclass


@dataclass
class Episode:
    title: str
    season: int
    episode_nr: str
    disk: int


file = open("StarTrekTNG.csv", "r")
episodes = []
for l in file.readlines()[1::]:
    e = l.split(";")
    episodes.append(Episode(e[0], int(e[1]), e[2], int(e[3])))

fragment = input("Nach welcher Folge soll gesucht werden?\n")
candidates = []
for e in episodes:
    if fragment.lower() in e.title.lower():
        candidates.append(e)
if candidates == []:
    print("Es konnten keine passenden Titel gefunden werden!")
for c in candidates:
    print(
        "Titel: "
        + c.title
        + "\n"
        + "Staffel: "
        + str(c.season)
        + "\n"
        + "Folge: "
        + c.episode_nr
        + "\n"
        + "Disk: "
        + "c.disk"
        + "\n\n"
    )

file.close()
