def is_palindrome(word):
    """
    Sprawdza, czy dany wyraz jest palindromem.
    
    Argument:
    word -- ciąg znaków (str), który chcemy sprawdzić
    
    Zwraca:
    True -- jeśli wyraz jest palindromem
    False -- jeśli wyraz nie jest palindromem
    """
    for i in range(len(word) // 2):
        if word[i] != word[-i-1]:
            return False
    return True
    
print(is_palindrome("kajak"))  # Oczekiwane: True
print(is_palindrome("potop"))  # Oczekiwane: True
print(is_palindrome("python"))  # Oczekiwane: False
