###########################################################################################
# Définir la fonction "nombreMajMin" qui compte le nombre de majuscules et de minuscules  #
###########################################################################################

import unittest

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
 
# # Tester l'algorithme
# caractere = "Activite1"
# # appel de la fonction et récupération des résultats
# maj,min= nombreMajMin(caractere)
# print("Nbre de majuscules :", maj)
# print("Nbre de minuscules :", min)



# unittest
#from nombreMajMin import nombreMajMin

class TestNombreMajMin(unittest.TestCase):
    def test_nombreMajMin(self):
        # Teste si la fonction compte correctement les majuscules et les minuscules dans une chaîne de caractères
        maj, min = nombreMajMin("Activite1")
        self.assertEqual(maj, 1)  # Il y a 2 majuscules dans "Activite1"
        self.assertEqual(min, 7)  # Il y a 6 minuscules dans "Activite1"

    def test_nombreMajMin_avecChaineVide(self):
        # Teste si la fonction traite correctement une chaîne vide
        maj, min = nombreMajMin("")
        self.assertEqual(maj, 0)  # Il ne devrait y avoir aucune majuscule dans une chaîne vide
        self.assertEqual(min, 0)  # Il ne devrait y avoir aucune minuscule dans une chaîne vide

    def test_nombreMajMin_avecCaracteresSpeciaux(self):
        # Teste si la fonction traite correctement les caractères spéciaux
        maj, min = nombreMajMin("!@#$%^&*()")
        self.assertEqual(maj, 0)  # Il ne devrait y avoir aucune majuscule dans cette chaîne
        self.assertEqual(min, 0)  # Il ne devrait y avoir aucune minuscule dans cette chaîne

if __name__ == '__main__':
    # Créer une suite de tests
    suite = unittest.TestLoader().loadTestsFromTestCase(TestNombreMajMin)

    # Créer un TestRunner
    test_runner = unittest.TextTestRunner()

    # Exécuter la suite de tests
    test_runner.run(suite)
