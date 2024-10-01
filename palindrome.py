def is_palindrome(word):
    """
    Sprawdza, czy dany wyraz jest palindromem.
    
    Argument:
    word -- ciąg znaków (str), który chcemy sprawdzić
    
    Zwraca:
    True -- jeśli wyraz jest palindromem
    False -- jeśli wyraz nie jest palindromem
    """
    return word == word[::-1]
    
print(is_palindrome("kajak"))  # Oczekiwane: True
print(is_palindrome("potop"))  # Oczekiwane: True
print(is_palindrome("python"))  # Oczekiwane: False
