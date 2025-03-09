def decrypt(ciphertxt, key):
    plaintxt = ''
    for letter in ciphertxt:
        if letter.isalpha():
            is_upper = letter.isupper()
            letter = letter.lower()
            index = letters.find(letter)
            new_index = (index - key) % num_letters
            new_letter = letters[new_index]
            plaintxt += new_letter.upper() if is_upper else new_letter
        else:
            plaintxt += letter
    return plaintxt
