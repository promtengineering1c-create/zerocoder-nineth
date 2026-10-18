VOWELS = frozenset('аеиоуыэюя')
def count_vowels(word: str) -> int:
    return sum(c in VOWELS for c in word.casefold().replace("ё", "е"))

print(count_vowels("Ежик"))