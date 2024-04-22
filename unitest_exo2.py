# Définir la fonction "nombreMajMin" qui compte le nombre de majuscules et de minuscules

def nombreMajMin(caractere):
# on initialise le nombre de majuscules et de minuscules à zéro
    maj = 0
    min = 0
# parcourir "caractere" en testant si le caractère est maj ou min
    for n in caractere:
# si le caractère est une majuscule
        if n.isupper():
            # incrémenter le compteur de majuscules
            maj = maj+1
            # si le caractère est une minuscule
        elif n.islower ():
            # incrémenter le compteur de minuscules
            min = min+1
            # retourner le nombre de majuscules et de minuscules
    return (maj, min)
 # Tester l'algorithme
caractere = "Activite1"
# appel de la fonction et récupération des résultats
maj,min= nombreMajMin(caractere)
print("Nbre de majuscules :", maj)
print("Nbre de minuscules :", min)