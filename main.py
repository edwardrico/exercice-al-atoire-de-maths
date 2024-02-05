import random
import time

NB_MIN = 0
NB_MAX = 5
QUESTION = 4
TEMPS_TOTAL = 30


def exercise_aleatoire():
    a = random.randint(NB_MIN, NB_MAX)
    b = random.randint(NB_MIN, NB_MAX)
    operateur = random.randint(1, 2)

    if operateur == 1:
        operateur = "+"
    elif operateur == 2:
        operateur = "-"
    elif operateur == 3:
        operateur = "*"
    elif operateur == 4:
        operateur = "/"

    resultat = eval(f"{a}{operateur}{b}")
    equation = float(input(f"Quel est le résultat de : {a} {operateur} {b} = "))
    if equation == resultat:
        return True
    else:
        print(f"La réponse correcte est : {resultat}")
        return False


points = 0
temps_debut = time.time()
for i in range(1, QUESTION + 1):
    temps_actuel = time.time()
    temps_ecoule = temps_actuel - temps_debut
    temps_restant = max(0, TEMPS_TOTAL - temps_ecoule)

    print(f"C'est parti, exercice n° {i}")
    print(f"Temps restant : {int(temps_restant)} secondes")
    if temps_ecoule >= TEMPS_TOTAL:
        print("Le temps est écoulé, vous avez perdu!")
        break
    time.sleep(1)
    if exercise_aleatoire():
        points += 1
        print(f"Réponse correcte, vous cumulez {points} point(s)")
    else:
        print("Réponse incorrecte")
    print()

pourcentage = (points / QUESTION) * 100
print(
    f"Vous avez un total de {points}/{QUESTION} points. Le questionnaire a un taux de réussite de {round(pourcentage)} %")
print()

if pourcentage == 100:
    print("Super, vous êtes trop bon en maths !")
elif pourcentage == 0:
    print("Vous devriez réviser vos maths, car vous n'êtes pas bon !")
elif pourcentage >= 50:
    print("Pas mal, vous êtes au-dessus de la moyenne !")
elif pourcentage <= 49:
    print("Vous devriez pratiquer plus !")
