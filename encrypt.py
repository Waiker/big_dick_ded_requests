# Функция для шифрования текста
def encrypt(text):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) + 3 - 65) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) + 3 - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def encrypt_files(directory):
    import os
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                text = file.read()
            encrypted_text = encrypt(text)
            with open(filepath, 'w') as file:
                file.write(encrypted_text)

encrypt_files('requests')