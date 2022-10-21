"""
Created on Tue Oct  11 11:02:00 2022

author: @curveo
"""

nbEleve = 13
ageEleve = 18
mots1 = "Il y a "
mots2 = " élèves dans la classe"
mots3 = " qui ont "
mots4 = " ans."
phrase = mots1 + str(nbEleve) + mots2 + mots3 + str(ageEleve) + mots4
phrase2 = ""
print(phrase)

variable1 = 1
variable2 = 2
variable3 = 3
variable4 = 4.2
variable5 = 5.2
variable6 = 6.2
variable7 = variable1 == 1
variable8 = variable2 == 2
variable9 = variable3 == 3
variable10 = "variable1 est = à 1"
variable11 = "variable2 est = à 2"
variable12 = "variable3 est = à 3"

print(variable1)
print(variable2)
print(variable3)
print(variable4)
print(variable5)
print(variable6)
print(variable7)
print(variable8)
print(variable9)
print(variable10)
print(variable11)
print(variable12)
print(type(variable1))
print(type(variable4))
print(type(variable7))
print(type(variable10))

if variable7 == True:
    print("variable1 est égale à 1")
else:
    print("variable1 n'est pas égale à 1")

if variable8 == True:
    print("variable2 est égale à 2")

if variable9 != True:
    print("variable3 n'est pas égale à 3")
else:
    print("variable3 est égale à 3")

while variable1 < 4:
    print("Dans le while")
    variable1 = variable1 + 1

for i in range(0, 3):
    print("Dans le for")

# bool4 = 3 = 6 | SyntaxError: cannot assign to literal
