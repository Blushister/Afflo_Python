import random

aleatoire = random.randint(0, 100)

debug = True
vs = False
tournois = False
manches = False
ia = False
stats = False
Multi_coop = True

def jeux_solo():
    a = random.randint(1, 100)
    icounter = 0
    if debug:
        print(a)
    while 1:
        player_nb = int(input("Nombre : "))
        if a < player_nb:
            print("Trop grand")
        elif a > player_nb:
            print("Trop petit")
        else:
            print(f"Le nombre est {a} et le nombre de tentative est {icounter}")
            break


def jeux_vs():
    a = random.randint(1, 100)
    if debug:
        print(a)
    playerround = 1
    icounter = 0
    while 1:
        icounter += 1
        if playerround == 1:
            player_nb = int(input("Player 1: "))
            playerround = 2
        else:
            player_nb = int(input("Player 2: "))
            playerround = 1
        if a < player_nb:
            print("Session 1 : Trop grand")
        elif a > player_nb:
            print("Session 1 : Trop petit")
        elif playerround == 2:
            print(f"Player 1 a win en {icounter}")
            break
        else:
            print(f"Player 2 a win en {icounter}")
            break


def mode_tournois(nb2):
    a = random.randint(1, nb2)
    b = random.randint(1, nb2)
    vp1 = 0
    vp2 = 0
    if debug:
        print(a)
        print(b)
    playerround = 1
    icounter = 0
    while 1:
        icounter += 1
        if playerround == 1:
            partie_player = playerround
            player_nb = int(input("Player 1: "))
            playerround = 2
        else:
            partie_player = playerround
            player_nb = int(input("Player 2: "))
            playerround = 1
        if partie_player == 1:
            if a < player_nb:
                print("Session 1 : Trop grand")
            elif a > player_nb:
                print("Session 1 : Trop petit")
            else:
                if manches:
                    print(f"Première victoire pour le joueur 1 en {icounter} coups.")
                    a = random.randint(1, nb2)
                    vp1 += 1
                    if debug:
                        print(a)
                    if vp1 == 3:
                        print("Player 1 win")
                        break

        else:
            if b < player_nb:
                print("Session 2 : Trop grand")
            elif b > player_nb:
                print("Session 2 : Trop petit")
            else:
                if manches:
                    print(f"Première victoire pour le joueur 2 en {icounter} coups.")
                    b = random.randint(1, nb2)
                    vp2 += 1
                    if debug:
                        print(b)
                    if vp2 == 3:
                        print("Player 2 win")
                        break


def iavsia(min, max):
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
            if debug:
                print("Trop grand")
            dmax = b
            b = random.randint(dmin, dmax)
        elif a > b:
            if debug:
                print("Trop petit")
            dmin = b
            b = random.randint(dmin, dmax)
        else:
            if debug:
                print(f"Le nombre est {a} et le nombre de tentative est {icounter}")
            return icounter


def Multiplayer_coop(nb):
    a = random.randint(0, nb)
    if debug:
        print(a)
    nb_player = int(input("Nombre de joueur : "))
    if nb_player > 4:
        print("Maximum 4 joueurs")
        return
    playerround = 1
    icounter = 0
    while 1:
        icounter += 1
        if nb_player == 2:
            if playerround == 1:
                player_nb = int(input("Player 1: "))
                playerround = 2
            else:
                player_nb = int(input("Player 2: "))
                playerround = 1
            if a < player_nb:
                print("Session 1 : Trop grand")
            elif a > player_nb:
                print("Session 1 : Trop petit")
            else:
                if playerround == 2:
                    print(f"Player 1 a win en {icounter}")
                    break
                else:
                    print(f"Player 2 a win en {icounter}")
                    break
        elif nb_player == 3:
            if playerround == 1:
                player_nb = int(input("Player 1: "))
                playerround = 2
            elif playerround == 2:
                player_nb = int(input("Player 2: "))
                playerround = 3
            else:
                player_nb = int(input("Player 3: "))
                playerround = 1
            if a < player_nb:
                print("Session 1 : Trop grand")
            elif a > player_nb:
                print("Session 1 : Trop petit")
            else:
                if playerround == 2:
                    print(f"Player 1 a win en {icounter}")
                    break
                elif playerround == 3:
                    print(f"Player 2 a win en {icounter}")
                    break
                else:
                    print(f"Player 3 a win en {icounter}")
                    break
        elif nb_player == 4:
            if playerround == 1:
                player_nb = int(input("Player 1: "))
                playerround = 2
            elif playerround == 2:
                player_nb = int(input("Player 2: "))
                playerround = 3
            elif playerround == 3:
                player_nb = int(input("Player 3: "))
                playerround = 4
            else:
                player_nb = int(input("Player 4: "))
                playerround = 1
            if a < player_nb:
                print("Session 1 : Trop grand")
            elif a > player_nb:
                print("Session 1 : Trop petit")
            else:
                if playerround == 2:
                    print(f"Player 1 a win en {icounter}")
                    break
                elif playerround == 3:
                    print(f"Player 2 a win en {icounter}")
                    break
                elif playerround == 4:
                    print(f"Player 3 a win en {icounter}")
                    break
                else:
                    print(f"Player 4 a win en {icounter}")
                    break

# def grandeur(a, x):
#     if a < x:
#         return 1
#     if a > x:
#         return 2
#     if a == x:
#         return 0
#
#
# def ia_Arnaud(a):
#     y = 0
#     z = 1000000
#     x = int(z - y / 2)
#     a = random.randint(y, z)
#     if debug:
#         print(a)
#     compteur = 1
#     while x != a:
#         compteur += 1
#         if grandeur(a, x) == 1:
#             y = x
#             x = int((z + y) / 2)
#         else:
#             z = x
#             x = int((z + y) / 2)
#     else:
#         print(f"C'est gagnée en {compteur} coups")
#         return compteur


def statistique():
    moyenne = 0
    for i in range(1000000):
        print(i)
        moyenne = moyenne + iavsia(0, 1000000)
        print(moyenne / 1000)


def main():
    if vs:
        print("Mode vs")
        jeux_vs()
    elif tournois:
        print("Mode tournois")
        mode_tournois(100)
    elif ia:
        print("Mode ia")
        iavsia()
    elif stats:
        print("Mode stats")
        statistique()
    elif Multi_coop:
        print("Mode Multiplayer coop")
        Multiplayer_coop(100)
    else:
        print("Mode solo")
        jeux_solo()

main()