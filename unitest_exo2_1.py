import unittest
from unittest.mock import patch
import sys
from io import StringIO

# Importer les fonctions que nous voulons tester
from unitest_exo2_0 import saisir_nombres, convertir_en_entiers, calculer_somme, afficher_resultats

class TestSommeNombres(unittest.TestCase):

    def setUp(self):
        # Rediriger la sortie standard vers un StringIO pour capturer les impressions
        self.output = StringIO()
        sys.stdout = self.output

    def tearDown(self):
        # Rétablir la sortie standard
        sys.stdout = sys.__stdout__

    def test_saisir_nombres(self):
        # Teste si la fonction saisir_nombres retourne deux chaînes de caractères
        with patch('builtins.input', side_effect=['5', '10']):
            nombre1, nombre2 = saisir_nombres()
            self.assertEqual(nombre1, '5')
            self.assertEqual(nombre2, '10')

    def test_convertir_en_entiers(self):
        # Teste si la fonction convertir_en_entiers convertit correctement les chaînes en entiers
        nombre1, nombre2 = convertir_en_entiers('5', '10')
        self.assertEqual(nombre1, 5)
        self.assertEqual(nombre2, 10)

    def test_calculer_somme(self):
        # Teste si la fonction calculer_somme retourne la somme correcte des nombres
        somme = calculer_somme(5, 10)
        self.assertEqual(somme, 15)

    def test_afficher_resultats(self):
        # Teste si la fonction afficher_resultats imprime les résultats correctement
        afficher_resultats(5, 10, 15)
        self.assertEqual(self.output.getvalue().strip(), 
                         "Vous avez saisi les nombres 5 et 10.\n"
                         "La somme de ces deux nombres est :\n"
                         "- En tant qu'entier : 15\n"
                         "- En tant que chaîne de caractères : 15\n"
                         "- En tant que nombre à virgule flottante : 15.00")

if __name__ == '__main__':
    unittest.main()
