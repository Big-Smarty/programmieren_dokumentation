from dataclasses import dataclass


@dataclass
class Country:
    country: str
    capitals: []


capitals = {}

countries_list = open("capitals.csv", "r")
for l in countries_list.readlines():
    temp = l.split(";")
    if temp == ["\n"]:
        continue
    capitals[temp[1]] = temp[0]

countries = []
for i in capitals:
    for j in capitals:
        if i == j:
            continue
        if capitals[i] == capitals[j]:
            countries.append(Country(capitals[i], [i, j]))

for c in countries:
    print(
        "Name des Landes: "
        + c.country
        + "\nName seiner Hauptstädte: \n"
        + c.capitals[0]
        + c.capitals[1]
    )
