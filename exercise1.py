def decrypt_caesar_cipher(ciphertext, tess_content):
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    found = False
    for shift in range(26):
        plaintext = ''
        for char in ciphertext:
            if char.upper() in ALPHABET: 
                index = (ALPHABET.index(char.upper()) - shift) % 26
                plaintext += ALPHABET[index] if char.isupper() else ALPHABET[index].lower()
            else:
                plaintext += char

        if plaintext in tess_content:
            print(f"Decryption finished at shift: {shift}, Plaintext: {plaintext}")
            found = True
            break   
    if not found:
        print("Decryption failed. No matching plaintext found.") 
        return

with open("inputfiles/tess26.txt", "r") as file:
    tess_content = file.read()

with open("inputfiles/personal_input/cexercise1.txt", "r") as file:
    ciphertext = file.read().strip() 

decrypt_caesar_cipher(ciphertext, tess_content)