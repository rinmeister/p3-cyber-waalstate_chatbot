import os
import configuraties as cnf

# vanuit de env wordt de key als string opgehaald en moeten we deze
# omzettten naar een integer. Dit kan met de int() functie.
key = cnf.secret_key  # Een waarde die in 8 bits past
print(key)

def encrypt(message):
    """Versleutelt een bericht met behulp van bitwise operatoren."""
    encrypted_chars = [] # Open een lege list of array

    for char in message:
        encrypted_char = (ord(char) ^ key) & 0xFF # ord geeft de ASCII waarde.
        encrypted_char = (encrypted_char << 3) | (encrypted_char >> 5)
        encrypted_char = encrypted_char & 0xFF  # Zorgt voor een 16-bit resultaat
        encrypted_chars.append(encrypted_char)
    return ",".join([str(i)for i in encrypted_chars]) # array to cd string

def decrypt(message):
    """Ontsleutelt een bericht met behulp van bitwise operatoren."""
    decrypted_chars = [] # Open een lege list of array

    # zet string om naar list met asciiwaarden.
    message = [int(i) for i in message.split(",")]

    # Herken in onderstaande code de omgekeerde volgorde van de encryptie.
    for char in message:
        decrypted_char = (char >> 3) | (char << 5) & 0xFF
        decrypted_char = (decrypted_char ^ key) & 0xFF
        decrypted_chars.append(chr(decrypted_char))
    return "".join(decrypted_chars)

def bruteforce(message, keys):
    """Ontsleutelt een bericht met behulp van bitwise operatoren."""
    decrypted_chars = [] # Open een lege list of array

    # zet asciiwaarden om naar array van integers
    message = [int(i) for i in message.split(",")]

    # Herken in onderstaande code de omgekeerde volgorde van de encryptie.
    for char in message:
        decrypted_char = (char >> 3) | (char << 5) & 0xFF
        decrypted_char = (decrypted_char ^ keys) & 0xFF
        decrypted_chars.append(chr(decrypted_char))
    return "".join(decrypted_chars)

