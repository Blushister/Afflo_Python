import random

def gamemulti(nb2):
    debug = True  # c'est la ligne pour activer le mode debug pour le jeu
    multi = True  # Jouer a plusieur ?
    tournois = False  # c'est la ligne pour activer le mode tournois pour le jeu | NB : requiere au minimum 2 joueurs
    vs = True  # c'est la ligne pour activer le mode vs pour le jeu | Si false ce sera du coop
    vp1 = 0
    vp2 = 0
    icounter = 0
    playerround = 1
    playerselect = 1
    if not multi:
        tournois = False
        vs = False
    if vs:
        a = random.randint(1, nb2)
        b = random.randint(1, nb2)
        if debug:
            print(a)
            print(b)
    else:
        a = random.randint(1, nb2)
        if debug:
            print(a)
    while 1:
        if multi:
            if playerround == 1:
                partie_player = playerround
                player_nb = int(input("Player 1: "))
                playerround = 2
            else:
                partie_player = playerround
                player_nb = int(input("Player 2: "))
                playerround = 1
        else:
            player_nb = int(input("Nombre : "))
        icounter = icounter + 1
        if vs:
            if partie_player == 1:
                print("test")
                if a < player_nb:
                    print("Session 1 : Trop grand")
                elif a > player_nb:
                    print("Session 1 : Trop petit")
                elif tournois:  # c'est la partie qui gere le mode tournois
                    print(f"Première victoire pour le joueur 1 en {icounter} coups.")
                    a = random.randint(1, nb2)
                    vp1 += 1
                    if debug:
                        print(a)
                    if vp1 == 3:
                        print("Player 1 win")
                        break
                else:
                    print(f"Player 1 a win en {icounter}")
                    break
            else:
                if b < player_nb:
                    print("Session 2 : Trop grand")
                elif b > player_nb:
                    print("Session 2 : Trop petit")
                elif tournois:  # c'est la partie qui gere le mode tournois
                    print(f"Première victoire pour le joueur 2 en {icounter} coups.")
                    b = random.randint(1, nb2)
                    vp2 += 1
                    if debug:
                        print(b)
                    if vp2 == 3:
                        print("Player 2 win")
                        break
                else:
                    print(f"Player 1 a win en {icounter}")
                    break
        else:
            if a < player_nb:
                print("Trop grand")
            elif a > player_nb:
                print("Trop petit")
            else:
                print(f"Le nombre est {a} et le nombre de tentative est {icounter}")
                break


gamemulti(100)
