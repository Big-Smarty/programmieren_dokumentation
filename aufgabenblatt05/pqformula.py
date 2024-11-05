from math import sqrt

q = float(input("q: "))
p = float(input("p: "))

if pow(p / 2, 2) < 2:
    print("Fehler: Keine reelle Lösung!")
else:
    x1 = -(p / 2) + sqrt(pow(p / 2, 2) - q)
    x2 = -(p / 2) - sqrt(pow(p / 2, 2) - q)
    print("x1: " + str(x1) + "\nx2: " + str(x2))
    print("x1²+px1+q = " + str(pow(x1, 2) + p * x1 + q))
    print("x2²+px2+q = " + str(pow(x2, 2) + p * x2 + q))
