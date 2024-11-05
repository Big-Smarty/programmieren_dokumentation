def to_bin(x):
    if x == 0:
        return "0"
    return str(x % 2) + to_bin(x // 2)


print(to_bin(int(input("Welche Zahl soll konvertiert werden?\n")))[::-1])
