def encrypt(plaintext, keyword):
    plaintext = plaintext.upper()  # Converting plaintext to uppercase for consistency
    keyword = keyword.upper()      # Converting keyword to uppercase for consistency

    encrypted_text = []

    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            shift = ord(keyword[i % len(keyword)]) - ord('A')
            encrypted_char = chr(((ord(plaintext[i]) - ord('A') + shift) % 26) + ord('A'))
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(plaintext[i])

    return ''.join(encrypted_text)

def decrypt(ciphertext, keyword):
    ciphertext = ciphertext.upper()  # Converting ciphertext to uppercase for consistency
    keyword = keyword.upper()        # Converting keyword to uppercase for consistency

    decrypted_text = []

    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            shift = ord(keyword[i % len(keyword)]) - ord('A')
            decrypted_char = chr(((ord(ciphertext[i]) - ord('A') - shift + 26) % 26) + ord('A'))
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(ciphertext[i])

    return ''.join(decrypted_text)