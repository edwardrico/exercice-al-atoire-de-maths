import random

NB_MIN = 0
NB_MAX = 10
QUESTION = 4


def exercise_aleatoire():
    a = random.randint(NB_MIN, NB_MAX)
    b = random.randint(NB_MIN, NB_MAX)
    operateur = random.randint(1, 4)

    if operateur == 1:
        operateur = "+"

    elif operateur == 2:
        operateur = "-"

    elif operateur == 3:
        operateur = "*"

    elif operateur == 4:
        operateur = "/"

    resultat = eval(f"{a}{operateur}{b}")
    equation = float(input(f"Quelle est le resultat de : {a} {operateur} {b} = "))
    if equation == resultat:
        return True
    else:
        print(f"La reponse correcter est : {resultat}")
        return False


points = 0

for i in range(0, QUESTION):
    print(f"C'est partie exercise n° {i + 1}")
    if exercise_aleatoire():
        points += 1
        print(f"reponse correcte, vous cumule {points} point ")

    else:
        print(f"Reponse incorrecte ")
    print()


pourcentage = (points/QUESTION) * 100
print(f"Vous avez une total de {points}/{QUESTION} points. Le que equibo a {round(pourcentage)} % de reusite")
print()

if pourcentage == 100:
    print("Super vous est trop bon est maths !")
elif pourcentage == 0:
    print("Vous devrie revise vos maths car, vous est pas bon !")
elif pourcentage >= 50:
    print("Pas mal vous est eu desus de la moyen!")
elif pourcentage <= 49:
    print("Vous devrei prectique plus !")
