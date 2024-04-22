######################################################################################################################
# Écrire un programme qui demande à l'utilisateur de saisir deux nombres sous forme de chaînes de caractères, 
# les convertit en entiers, effectue la somme de ces deux nombres, puis affiche le résultat sous différentes formes.
######################################################################################################################

def saisir_nombres():
    nombre1 = input("Entrez le premier nombre : ")
    nombre2 = input("Entrez le deuxième nombre : ")
    return nombre1, nombre2

def convertir_en_entiers(nombre1, nombre2):
    nombre1 = int(nombre1)
    nombre2 = int(nombre2)
    return nombre1, nombre2

def calculer_somme(nombre1, nombre2):
    somme = nombre1 + nombre2
    return somme

def afficher_resultats(nombre1, nombre2, somme):
    print("Vous avez saisi les nombres {} et {}.".format(nombre1, nombre2))
    print("La somme de ces deux nombres est :")
    print("- En tant qu'entier : {}".format(somme))
    print("- En tant que chaîne de caractères :", str(somme))
    print("- En tant que nombre à virgule flottante : {:.2f}".format(float(somme)))

def main():
    nombre1, nombre2 = saisir_nombres()
    nombre1, nombre2 = convertir_en_entiers(nombre1, nombre2)
    somme = calculer_somme(nombre1, nombre2)
    afficher_resultats(nombre1, nombre2, somme)

main()
