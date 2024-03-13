def decrypt_caesar_cipher(ciphertext):
    decrypted = ciphertext
    return decrypted

def validateDecryptedText(decryptedText):
    with open("inputfiles/tess26.txt", "r") as file:
        tess_content = file.read()
    return decryptedText in tess_content


with open("inputfiles/personal_input/cexercise2.txt", "r") as file:
    ciphertext = file.read().strip() 

decryptedText = decrypt_caesar_cipher(ciphertext)
success = validateDecryptedText(decryptedText)

if success:
    print(f"Decryption finished with plaintext: {decryptedText}")
else:
    print(f"Decryption failed with plaintext: {decryptedText} No matching plaintext found.") 
