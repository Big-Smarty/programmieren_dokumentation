def test_nächster_geburtstag() -> None:
    from classes_fortsetzung import Person
    from datetime import date

    """Test um zu überprüfen ob die Funktion auch den richtigen nächsten Geburtstag ausspuckt"""
    budi = Person("Budeanu", "Daniel", date(2005, 4, 8))
    assert budi.nächster_geburtstag == date(2025, 4, 8)
    budi2 = Person("Daniel", "Budeanu", date(2005, 12, 12))
    assert budi2.nächster_geburtstag == date(2025, 12, 12)


def test_einfügen() -> None:
    """Test um zu überprüfen ob Personen richtig eingefügt werden"""
    from classes_fortsetzung import Person, Personendatenbank
    from datetime import date

    pdb = Personendatenbank([])
    budi = Person("Budeanu", "Daniel", date(2005, 4, 8))
    pdb.einfügen(budi)
    assert pdb.findePerson("Budeanu", "Daniel") == budi


def test_nächste_geburtstage() -> None:
    """Test um zu überprüfen ob der nächste Geburtstag richtig errechnet und Personen anschließend richtig sortiert werden"""
    from classes_fortsetzung import Person, Personendatenbank
    from datetime import date

    pdb = Personendatenbank([])
    budi = Person("Budeanu", "Daniel", date(2005, 4, 8))
    pdb.einfügen(budi)
    a = Person("a", "b", date(2005, 1, 30))
    pdb.einfügen(a)
    b = Person("c", "d", date(1999, 2, 22))
    pdb.einfügen(b)
    c = Person("e", "f", date(1829, 5, 15))
    pdb.einfügen(c)
    d = Person("g", "h", date(1120, 11, 11))
    pdb.einfügen(d)
    e = Person("i", "j", date(2000, 12, 31))
    pdb.einfügen(e)
    f = Person("k", "l", date(2012, 3, 3))
    pdb.einfügen(f)
    g = Person("m", "n", date(2022, 5, 7))
    pdb.einfügen(g)

    print(pdb.nächste_geburtstage())

    assert (
        pdb.nächste_geburtstage()
        == sorted(pdb.personen, key=lambda person: person.nächster_geburtstag)[:5:]
    )
