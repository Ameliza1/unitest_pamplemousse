# Import de pytest
import pytest

# Vos fonctions de vérification de palindrome et de comptage de palindrome

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



# Tests avec pytest

def test_est_palindrome():
    assert est_palindrome("radar") == True
    assert est_palindrome("bonjour") == False
    assert est_palindrome("kayak") == True
    assert est_palindrome("été") == True
    assert est_palindrome("elle") == True
    assert est_palindrome("reconnaître") == False

def test_compter_palindromes():
    mots_1 = ["radar", "bonjour", "kayak", "été", "elle", "reconnaître"]
    mots_2 = ["bonjour", "été", "kayak", "elle", "reconnaître"]
    mots_3 = ["radar", "radar", "radar", "radar"]
    
    assert compter_palindromes(mots_1) == 8
    assert compter_palindromes(mots_2) == 3
    assert compter_palindromes(mots_3) == 4
