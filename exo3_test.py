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

import unittest

class TestPalindrome(unittest.TestCase):
    def test_est_palindrome(self):
        self.assertTrue(est_palindrome("radar"))
        self.assertFalse(est_palindrome("bonjour"))
        self.assertTrue(est_palindrome("kayak"))
        self.assertTrue(est_palindrome("été"))
        self.assertTrue(est_palindrome("elle"))
        self.assertFalse(est_palindrome("reconnaître"))

    def test_compter_palindromes(self):
        mots_1 = ["radar", "bonjour", "kayak", "été", "elle", "reconnaître"]
        mots_2 = ["bonjour", "été", "kayak", "elle", "reconnaître"]
        mots_3 = ["radar", "radar", "radar", "radar"]
        
        self.assertEqual(compter_palindromes(mots_1), 4)
        self.assertEqual(compter_palindromes(mots_2), 3)
        self.assertEqual(compter_palindromes(mots_3), 5)

if __name__ == '__main__':
    unittest.main()
