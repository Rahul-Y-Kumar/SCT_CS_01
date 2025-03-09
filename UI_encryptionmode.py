rint("\n" + "-"*84)
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
