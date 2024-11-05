speisekarte = {
    "Stilles Wasser": 2.90,
    "Mineralwasser": 2.90,
    "Cola": 2.90,
    "Bitter Lemon": 3.60,
    "Orangensaft": 3.90,
    "Espresso": 2.30,
    "Heiße Schokolade": 4.10,
    "Salat": 6.50,
    "Flädlesuppe": 6.50,
    "Maultaschen": 16.80,
    "Kässpätzle": 15.30,
    "Schweinelendchen": 23.90,
    "Ofenkartoffeln": 14.90,
    "Gebratener Ziegenkäse": 15.50,
}

sum = 0
for x in speisekarte:
    print(x)

while True:
    dish = input("Welches Gericht hätten sie gerne?\n")
    if dish == "":
        break
    if not dish in speisekarte:
        print("Dieses Gericht haben wir nicht!")
        continue
    sum += speisekarte[dish]
print("Ihre Endsumme: " + str(sum))
