def encrypt(text, s):
    cipher = ""

    for char in text:
        if char.isupper():
            cipher += chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower():
            cipher += chr((ord(char) + s - 97) % 26 + 97)
        else:
            cipher += char  # Non-alphabetic characters remain unchanged

    return cipher

def decrypt(cipher, s):
    plain = ""

    for char in cipher:
        if char.isupper():
            plain += chr((ord(char) - s - 65) % 26 + 65)
        elif char.islower():
            plain += chr((ord(char) - s - 97) % 26 + 97)
        else:
            plain += char  # Non-alphabetic characters remain unchanged

    return plain

# Taking input from the user
text = input("Enter a message you want to encrypt: ")
shift = input("Enter a shift value: ")
s = int(shift)

# Printing results
print("Text: " + text)
print("Shift: " + str(s))
print("Cipher: " + encrypt(text, s))
print("Decrypted Message: " + decrypt(encrypt(text, s), s))
