import string

encoded_text = input("Enter text to decode : ")

def caesar_cipher(text, shift):
    alphabet = string.ascii_letters + string.digits + string.punctuation

    for c in text:
        if c in alphabet:
            index = alphabet.find(c)
            new_index = (index + shift)
            yield alphabet[new_index]
        else:
            yield c

print("----- BRUTE FORCING CAESAR CIPHER -----")
for shift in range(26):
    print("".join(caesar_cipher(encoded_text, shift)))
