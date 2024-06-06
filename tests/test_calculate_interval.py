import pytest
from chord_generator import calculate_interval  
from chord_generator import chords
# importation des fonctions
# importation dictonaire

def test_calculate_interval():
    assert calculate_interval(60, 64) == 4, "Should return 4 for C4 to E4"
    assert calculate_interval(70, 65) == -5, "Should return -5 for B4 to F4"
# Test avec des valeurs qui devraient retourner un intervalle correct
    assert calculate_interval(60, 70) != 0, "Should not return 0 for different notes"
    assert calculate_interval(72, 72) == 0, "Should return 0 for the same note"
# Test avec des valeurs où l'intervalle ne devrait pas être un certain résultat
    # Test pour vérifier la manipulation des entrées négatives ou non valides
    with pytest.raises(TypeError):
        calculate_interval('a', 72)  # Entrée non valide doit lever une exception


