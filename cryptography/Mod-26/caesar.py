def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # アルファベット文字のみを処理
            if char.isupper():
                # 大文字の場合
                decrypted_char = chr((ord(char) - shift - 65) % 26 + 65)
            else:
                # 小文字の場合
                decrypted_char = chr((ord(char) - shift - 97) % 26 + 97)
            plaintext += decrypted_char
        else:
            # アルファベット以外の文字はそのまま追加
            plaintext += char
    return plaintext

# 使用例
ciphertext = input("ciphertext: ")
shift = int(input("shift: "))

decrypted_text = caesar_decrypt(ciphertext, shift)
print(decrypted_text)
