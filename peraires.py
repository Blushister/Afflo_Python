"""
Created on Tue Oct  18 9:47:24 2022

author: @curveo
"""
import math


# Special

def pythagore(a, b):
    a = a / 2
    c = pow(a, 2) + pow(b, 2)
    c = math.sqrt(c)
    print(f"Le résultat de Pythagore est: {c}")
    return c


# Calcule des aire

def aircarrer(a):
    aire = a * a
    print(f"L'aire du carré est: {aire}")
    return aire


def airtriangle(a, b):
    h = pythagore(a, b)
    aire = (a * h)
    print(f"L'aire du triangle est: {aire}")
    return aire


def airrectangle(a, b):
    aire = a * b
    print(f"L'aire du rectangle est: {aire}")
    return aire


def aircercle(r):
    aire = math.pi * math.puissance(r, 2)
    print(f"L'aire du cercle est: {aire}")
    return aire


def airdemicercle(r):
    aire = (math.pi * r ** 2) / 2
    print(f"L'aire du demi cercle est: {aire}")
    return aire


# Calcule des perimètres

def pericarrer(a):
    perimetre = a * 4
    print(f"Le périmètre du carré est: {perimetre}")
    return perimetre


def perirectangle(a, b):
    perimetre = (a * 2) + (b * 2)
    print(f"Le périmètre du rectangle est: {perimetre}")
    return perimetre


def peritriangle(a, b, c):
    perimetre = a + b + c
    print(f"Le périmètre du triangle est: {perimetre}")
    return perimetre


def pericercle(r):
    perimetre = 2 * math.pi * r
    print(f"Le périmètre du cercle est: {perimetre}")
    return perimetre


def peridemicercle(r):
    perimetre = math.pi * r
    print(f"Le périmètre du demi cercle est: {perimetre}")
    return perimetre


# Calculer des volumes

def volumesphere(r):
    volume = 4 * math.pi * math.puissance(r, 3) / 3
    print(f"Le volume de la sphère est: {volume}")
    return volume


def volumecylindre(r, h):
    volume = math.pi * math.puissance(r, 2) * h
    print(f"Le volume du cylindre est: {volume}")
    return volume


def volumepyramidebasecercle(r, h):
    volume = (math.pi * math.puissance(r, 2) * h) / 3
    print(f"Le volume de la pyramide est: {volume}")
    return volume


def volumepyramidebasecarrer(a, h):
    volume = (math.puissance(a, 2) * h) / 3
    print(f"Le volume de la pyramide est: {volume}")
    return volume


def volumecube(a):
    volume = math.puissance(a, 3)
    print(f"Le volume du cube est: {volume}")
    return volume


def airFigure1():
    rect = airrectangle(3, 4)
    tri1 = airtriangle(6, 4)
    demic = airdemicercle(3)
    big_rect = airrectangle(16, 6)
    result = big_rect + (demic * 2) + (tri1 * 2) - rect
    return result


def periFigure1():
    rect = perirectangle(3, 4)
    tri1 = peritriangle(3, 4, 5)
    demic = peridemicercle(3)
    big_rect = perirectangle(16, 6)
    result = big_rect + (demic * 2) + ((tri1 * 2) - 6) + (rect - 4)
    return result


z = periFigure1()
print(z)
