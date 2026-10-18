import pytest
from main import count_vowels


@pytest.mark.parametrize('word, result', [
    ("Привет", 2),
    ("Ёжик", 2),
    ("", 0),
    ("123 !?", 0)
])
def test_count_vowels(word, result):
    assert count_vowels(word) == result

    
    


