import math
# Coin des Function

def addition(nb1, nb2):
    return nb1 + nb2


def subtraction(nb1, nb2):
    return nb1 - nb2


def multiplication(nb1, nb2):
    return nb1 * nb2


def division(nb1, nb2):
    return nb1 / nb2


def puissance(nb1, nb2):
    return nb1 ** nb2

def racine(nb1):
    return nb1 ** 0.5

# Coin des Procedure

def addition_proc(nb1, nb2):
    print(f"Le résultat de l'addition est: {nb1 + nb2}")


def subtraction_proc(nb1, nb2):
    print(f"Le résultat de la soustraction est: {nb1 - nb2}")


def multiplication_proc(nb1, nb2):
    print(f"Le résultat de la multiplication est: {nb1 * nb2}")


def division_proc(nb1, nb2):
    print(f"Le résultat de la division est: {nb1 / nb2}")

def puissance_proc(nb1, nb2):
    print(f"Le résultat de la puissance est: {nb1 ** nb2}")

def myname(name):
    print("Bonjour " + name)

# Main code

print("Ici c'est les fonctions ")

# addition(float(input("Nombre 1 : ")), float(input("Nombre 2 : ")))
# subtraction(float(input("Nombre 1 : ")), float(input("Nombre 2 : ")))
# multiplication(float(input("Nombre 1 : ")), float(input("Nombre 2 : ")))
# division(float(input("Nombre 1 : ")), float(input("Nombre 2 : ")))
# puissance(float(input("Nombre 1 : ")), float(input("Nombre 2 : ")))
#
# print("Ici c'est les procedure ")
#
# addition_proc(float(input("Nombre 1 : ")), float(input("Nombre 2 : ")))
# subtraction_proc(float(input("Nombre 1 : ")), float(input("Nombre 2 : ")))
# multiplication_proc(float(input("Nombre 1 : ")), float(input("Nombre 2 : ")))
# division_proc(float(input("Nombre 1 : ")), float(input("Nombre 2 : ")))
# puissance_proc(float(input("Nombre 1 : ")), float(input("Nombre 2 : ")))
myname(input("Entrez votre nom : "))

# create fonction pythagore
def pythagore(a, b):
    return math.sqrt(a ** 2 + b ** 2)
