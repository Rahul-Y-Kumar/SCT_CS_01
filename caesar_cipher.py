letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

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


print("\n" + "-"*84)
print(" *** CAESAR CIPHER PROGRAM *** ".center(84))
print("-"*84 + "\n")

print("Do you want to Encrypt or Decrypt?")
user_input = input('Enter "e" for Encryption or "d" for Decryption: ').lower()
print()

if user_input == 'e':
    print("__ENCRYPTION MODE ACTIVATED__".center(84))
    print("-"*84 + "\n")
    Key = int(input("Enter the key value (1-26): "))
    print()
    text = input("Enter the text to Encrypt: ")
    ciphertxt = encrypt(text, Key)
    print("\nEncrypted Text:", ciphertxt)
    print("-"*84 + "\n")


elif user_input == 'd':
    print("__DECRYPTION MODE ACTIVATED__".center(84))
    print("-"*84 + "\n")
    Key = int(input("Enter the key value (1-26): "))
    print()
    text = input("Enter the text to Decrypt: ")
    plaintxt = decrypt(text, Key)
    print("\nDecrypted Text:", plaintxt)
    print("-"*84 + "\n")

else:
    print("Invalid choice! Please enter 'e' or 'd'.")

