# Definition des variables

test : int = 1
a = 8
b = 16
a = b
nom1 = "Alice"
nom2 = "Bob"
temp = nom2
nom2 = nom1
nom1 = temp

# On affiche les variables et on les manipules
print(test)
print(nom1)
print(nom2)
nom1, nom2 = nom2, nom1
print(nom1)
print(nom2)
print(a)
print(b)
b = b + a
print(a)
print(b)
