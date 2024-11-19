def vektor_summe(a, b):
    """Addiere die Vektoren elementweise (a0, a1, a2) und (b0, b1, b2) werden zu (a0+b0, a1+b1, a2+b2)"""
    out = []
    for i in range(len(a)):
        out.append(a[i] + b[i])
    return out


def skalar_produkt(a, b):
    """Errechne das Skalarprodukt der Vektoren a und b"""
    out = []
    sum = 0
    for i in range(len(a)):
        out.append(a[i] * b[i])
    for i in out:
        sum += out
    return sum


def skaliere(k, a):
    """Multipliziere alle Elemente in a mit k sodass (a0, a1, a2) und k zu (a0*k, a1*k, a2*k) werden"""
    for i in range(len(a)):
        a[i] *= k
    return a
