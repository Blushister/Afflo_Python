import random

debug = False


def iav1(min, max):
    dmin = min
    dmax = max
    a = random.randint(min, max)
    b = random.randint(dmin, dmax)
    icounter = 0
    if debug:
        print(a)
        print(b)
    while 1:
        icounter += 1
        if a < b:
            print("Trop grand")
            dmax = b
            b = random.randint(dmin, dmax)
        elif a > b:
            print("Trop petit")
            dmin = b
            b = random.randint(dmin, dmax)
        else:
            print(f"Le nombre est {a} et le nombre de tentative est {icounter}")
            return icounter


iav1(0, 100)
