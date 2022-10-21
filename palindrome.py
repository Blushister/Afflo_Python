def palindrome(string):
    a = string.lower().replace(" ", "").replace(",", "").replace(".", "") \
        .replace("!", "").replace("?", "").replace(";", "").replace(":", "") \
        .replace("(", "").replace(")", "").replace("[", "").replace("]", "") \
        .replace("{", "").replace("}", "").replace("'", "").replace('-', "")
    c = a[::-1]
    index = 0
    i = len(a) - 1
    while index != len(a):
        car1 = a[index]
        car2 = c[index]
        print(f"car1: {car1}")
        print(f"car2: {car2}")
        if car1 == car2:
            print("ok")
            index += 1
        elif car1 != car2:
            print("Ce n'est pas un palindrome")
            return
    print("c'est un palindrome")


palindrome("Élu par cette crapule")
palindrome("Émile nu a une lime")
palindrome("Était-ce un chat que je vois là ?")
palindrome("Engage le jeu, que je le gagne")
palindrome("Tu l'as trop été, Port-salut")
palindrome("L'été indien")
