# New projet
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 10:00:00 2019

author: @curveo
"""


def puissance(nombre, exposant):
    resultat = nombre ** exposant
    return resultat


def puissancemoi(nombre, exposant):
    p = 1
    resultat = nombre
    while p < exposant:
        resultat = resultat * nombre
        p = p + 1
    return resultat


calcul = 877 // 121
print(calcul)
calcul2 = 877 % 121
print(calcul2)
print(puissance(2, 2))
print(puissance(2, 8))
print(puissance(8, 4) + (puissance(9, 3)))
print(puissancemoi(2, 2))
print(pow(2, 2))

