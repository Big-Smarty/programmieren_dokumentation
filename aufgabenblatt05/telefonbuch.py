def binary_search(region, name):
    if name.lower() == region[(len(region) - 1) // 2][0].lower():
        return region[(len(region) - 1) // 2]

    if name.lower() < region[(len(region) - 1) // 2][0].lower():
        return binary_search(region[: (len(region) - 1) // 2 - 1], name)

    if name.lower() > region[(len(region) - 1) // 2][0].lower():
        return binary_search(region[(len(region) + 1) // 2 - 1 : :], name)


entries = []
book = open("telefonbuch.csv", "r")
for l in book.readlines()[1::]:
    temp = l.split(";")
    if temp == ["\n"]:
        continue
    entries.append((temp[0], temp[1], temp[2]))

fragment = input("Nach welchem Namen suchen sie?\n")
out = binary_search(entries, fragment)
print("Name: " + out[0] + " " + out[1] + "\nTelefonnummer: " + out[2])
