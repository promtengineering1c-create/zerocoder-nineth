# создать переменную cleaned_text, черзе копирование из исходного текста буквенно-цифровыъ символов и перевод их в нижний регистр (цикл for, lower, isalnum)
# возращем выражение сравнения очищенной переменной и перевернутого среза этой переменной 

def is_palindrome(text: str) -> bool:
  cleaned_text = "".join(c.lower() for c in text if c.isalnum())
  return cleaned_text == cleaned_text[::-1]


print(is_palindrome("шалаш"))  
print(is_palindrome("А роза упала на лапу Азора"))  
print(is_palindrome("привет"))  