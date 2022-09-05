# Vigenere Cupher

def getChar(code: int) -> str:
    return chr(code % 26 + 97)

def getCode(char: str) -> int:
    return (ord(char) - 97)


def encrypt(plainText:str, key:str) -> str:
    cipher = ''

    splitText = []
    for char in plainText:
        splitText.append(char)

    splitKey = []

    i = 0
    for _ in splitText:
        splitKey.append(key[i % len(key)])
        i += 1

    splitText = [getCode(i) for i in splitText]
    splitKey = [getCode(i) for i in splitKey]

    splitCipher = []

    for i in range(len(splitKey)):
        splitCipher.append(splitText[i] + splitKey[i])

    splitCipher = [getChar(i) for i in splitCipher]

    for char in splitCipher:
        cipher += char

    return cipher


def decrypt(cipherText:str, key:str) -> str:
    message = ''

    splitText = []
    for char in cipherText:
        splitText.append(char)

    splitKey = []

    i = 0
    for _ in splitText:
        splitKey.append(key[i % len(key)])
        i += 1

    splitText = [getCode(i) for i in splitText]
    splitKey = [getCode(i) for i in splitKey]

    splitCipher = []

    for i in range(len(splitKey)):
        splitCipher.append(splitText[i] - splitKey[i])

    splitCipher = [getChar(i) for i in splitCipher]

    for char in splitCipher:
        message += char

    return message


if __name__ == "__main__":
    # message = input('Enter your message: ')
    # key = input('Enter key: ')
    message = 'wearediscoveredsaveyourself'
    key = 'deceptive'

    cipher = encrypt(message.lower(), key.lower())
    print(cipher)

    message = decrypt(cipher.lower(), key.lower())
    print(message)
