import math
import random


def vraiFalse(nb):
    return nb > 99


def fonct_vraiFalse(nb):
    print(nb > 99)


def proc_supoupas(a, b):
    if a > b:
        print("a>b")
    elif a < b:
        print("a<b")


def proc_maisdemandemoi():
    a = input("a: ")
    b = input("b: ")
    if a > b:
        print("a>b")
    else:
        print("a<b")


def croissant(a, b, c):
    if a < b < c:
        print(a, b, c)
    elif a < c < b:
        print(a, c, b)
    elif b < a < c:
        print(b, a, c)
    elif b < c < a:
        print(b, c, a)
    elif c < a < b:
        print(c, a, b)
    elif c < b < a:
        print(c, b, a)


def tac():
    a = int(input("Nombre 1 : "))
    if a > 0:
        tac()
    else:
        b = a ** 2
        print(b)


def devinenoopti(nb) -> int:
    icounter = 0
    a = random.randint(1, nb)
    nb = 100
    while 1:
        icounter += 1
        b = nb
        if a < b:
            print("trop grand")
            nb = nb - 1
        if a > b:
            print("trop petit")
            nb = nb + 1
        if a == b:
            print(f"gagné en {icounter} coups")
            break
    return icounter


def devineopti(nb) -> int:
    icounter = 0
    a = random.randint(1, nb)
    nb = 100
    while 1:
        icounter += 1
        b = nb
        if a < b:
            print("trop grand")
            nb = nb - 10
        if a > b:
            print("trop petit")
            nb = nb + 1
        if a == b:
            print(f"gagné en {icounter} coups")
            break
    return icounter


def moyenne():
    somme = 0
    somme2 = 0
    for i in range(1000):
        somme += devinenoopti(100) / 1000
        somme2 += devineopti(100) / 1000
    print(f"moyenne devinenoopti: {somme}")
    print(f"moyenne devineopti: {somme2}")

croissant("z", "a", "b")