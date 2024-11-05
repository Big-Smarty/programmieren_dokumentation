from dataclasses import dataclass


@dataclass
class Entry:
    char: str
    count: int

    def __lt__(self, other):
        return self.char < other.char


word1 = input("Wort 1: \n")
word2 = input("Wort 2: \n")


if word1.lower() == word2.lower():
    print("beide Worte sind gleich!")

if len(word1) != len(word2):
    print("Die Worte haben unterschiedlich viele Buchstaben!")

entries1 = []
for w in word1.lower():
    existing = False
    for e in entries1:
        if w == e.char:
            existing = True
            e.count += 1
    if existing:
        continue
    entries1.append(Entry(w, 1))


entries2 = []
for w in word2.lower():
    existing = False
    for e in entries2:
        if w == e.char:
            existing = True
            e.count += 1
    if existing:
        continue
    entries2.append(Entry(w, 1))

if sorted(entries1) == sorted(entries2):
    print("Die eingegebenen Worte sind Anagramme!")
