# Функция для расшифровки текста
def decrypt(text):
    # Ваш код для расшифровки текста
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                decrypted_text += chr((ord(char) - 3 - 65) % 26 + 65)
            else:
                decrypted_text += chr((ord(char) - 3 - 97) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text

# Функция для расшифровки текстовых файлов в каталоге
def decrypt_files(directory):
    import os
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                text = file.read()
            decrypted_text = decrypt(text)
            with open(filepath, 'w') as file:
                file.write(decrypted_text)
