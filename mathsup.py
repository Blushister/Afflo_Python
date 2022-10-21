"""
Created on Tue Oct  18 09:12:00 2022

author: @curveo
"""


# Coin des fonctions


def fonctionmath(nb1):
    f = (2 * nb1) + 4
    print(f"Le résultat de la fonction math est: {f}")
    return f

def fonctiony(a, b, x):
    y = a * x + b
    print(f"Le résultat de la fonction y est: {y}")
    return y


fonctiony(float(input("a : ")), float(input("b : ")), float(input("x : ")))

# fonctionmath(float(input("Entrez un nombre: ")))
#
# fonction1 = fonctionmath(-2)
# fonction2 = fonctionmath(0)
# fonction3 = fonctionmath(10)
#
# print(fonction1 + fonction2 + fonction3)
