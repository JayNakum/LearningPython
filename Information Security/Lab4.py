# Vigenere Cipher
# Experiment 5

def getChar(code:int) -> str:
    return chr(code % 26 + 97)

def getCode(char:str) -> int:
    return (ord(char) - 97)


def encrypt(plainText:str, key:str) -> str:
    cipher = ''

    splitText = [getCode(char) for char in plainText]

    splitKey = []
    i = 0
    for _ in splitText:
        splitKey.append(getCode(key[i % len(key)]))
        i += 1

    splitCipher = []
    for i in range(len(splitKey)):
        splitCipher.append(getChar(splitText[i] + splitKey[i]))

    for char in splitCipher:
        cipher += char

    return cipher


def decrypt(cipherText:str, key:str) -> str:
    message = ''

    splitText = [getCode(char) for char in cipherText]

    splitKey = []
    i = 0
    for _ in splitText:
        splitKey.append(getCode(key[i % len(key)]))
        i += 1

    splitCipher = []
    for i in range(len(splitKey)):
        splitCipher.append(getChar(splitText[i] - splitKey[i]))

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
