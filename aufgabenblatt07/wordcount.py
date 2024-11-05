import re
from dataclasses import dataclass


@dataclass
class Entry:
    word: str
    count: int

    def __lt__(self, other):
        self.count < other.count


with open("shes-always-a-woman.txt", "r", encoding="utf-8") as infile:
    lyrics = infile.read()
words = list(map(lambda s: s.lower(), re.split(r"\W+", lyrics)))
entries = []
for w in words:
    existing = False
    for e in entries:
        if w == e.word:
            existing = True
            e.count += 1
    if existing:
        continue
    entries.append(Entry(w, 1))

idx = 0
for i in range(len(entries)):
    if entries[idx].count > entries[i].count:
        continue
    if entries[idx].count < entries[i].count:
        idx = i
print("Das am häufigste vorkommende Wort: " + entries[idx].word)
