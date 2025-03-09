def encrypt(plaintxt, key):
    ciphertxt = ''
    for letter in plaintxt:
        if letter.isalpha():  
            is_upper = letter.isupper()  
            letter = letter.lower()  
            index = letters.find(letter)
            new_index = (index + key) % num_letters  
            new_letter = letters[new_index]
            ciphertxt += new_letter.upper() if is_upper else new_letter  
        else:
            ciphertxt += letter  
    return ciphertxt
