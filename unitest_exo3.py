
import unittest

# Écrivez un programme qui compte combien de mots dans une liste sont des palindromes. 
# Un palindrome est un mot qui se lit de la même manière de gauche à droite et de droite à gauche.

def est_palindrome(mot):
    """
    Vérifie si un mot est un palindrome.
    """
    return mot == mot[::-1]

def compter_palindromes(liste_mots):
    """
    Compte le nombre de mots palindromes dans une liste de mots.
    """
    count = 0
    for mot in liste_mots:
        if est_palindrome(mot):
            count += 1
    return count

# Important : 
# ici j'ai crée 2 fonctions
# fct est_palindrome : elle sert à déterminer si un mot est palindrome 
# (un palindrome est un mot qui se lit dans les 2 sens)
# fct compter_plaindromes : intialiser à 0, elle incrémente +1 à chaque fois qu'elle trouve un palindrome dans la liste 


######## unitest ########


# Votre code existant ici...

class TestPalindrome(unittest.TestCase):
    def test_est_palindrome(self):
        self.assertTrue(est_palindrome("radar"))
        self.assertFalse(est_palindrome("bonjour"))
        self.assertTrue(est_palindrome("kayak"))
        self.assertTrue(est_palindrome("été"))
        self.assertTrue(est_palindrome("elle"))
        self.assertTrue(est_palindrome("reconnaître"))

    def test_compter_palindromes(self):
        mots_1 = ["radar", "bonjour", "kayak", "été", "elle", "reconnaître"]
        mots_2 = ["bonjour", "été", "kayak", "elle", "reconnaître"]
        mots_3 = ["radar", "radar", "radar", "radar"]
        
        self.assertEqual(compter_palindromes(mots_1), 5)
        self.assertEqual(compter_palindromes(mots_2), 4)
        self.assertEqual(compter_palindromes(mots_3), 4)

if __name__ == '__main__':
    unittest.main()

