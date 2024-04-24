import pytest

# Définition d'une fonction de test paramétrée
@pytest.mark.parametrize("entree,attendu", [
    ("hello", 5),
    ("world", 5),
    ("pytest", 6),
])
def test_longueur_chaine(entree, attendu):
    assert len(entree) == attendu
