import pytest

from chord_generator import pick_random_chord, calculate_interval

from chord_generator import chords

@pytest.fixture
def get_chords_Cmin():
    return [48, 51, 55]

@pytest.fixture
def get_chords_Emaj():
    return [52, 56, 59]


def test_pick_random_chord():
    chord = pick_random_chord()
    assert chord in chords

def test_pick_not_in_chi_chord():
    not_chord = 'Cmin42'
    assert not_chord not in chords

def test_calculate_interval(get_chords_Cmin, get_chords_Emaj):
    interval = calculate_interval(get_chords_Cmin[0], get_chords_Emaj[0])
    assert interval == 4
    assert calculate_interval(-8, -9) == 1