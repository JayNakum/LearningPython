# Hill Cipher

import numpy as np

def getChar(code:int) -> str:
    return chr(code % 26 + 97)

def getCode(char:str) -> int:
    return (ord(char) - 97) % 26

def getKeyMatrix(key: str, n: int) -> list:
    keyMatrix = []

    i = 0
    while (i < len(key)):
        row = []
        for _ in range(n):
            row.append(getCode(key[i]))
            i += 1
        keyMatrix.append(row)

    # print(keyMatrix)
    return keyMatrix

def getMessageVectors(message: str, n: int) -> list:
    while (len(message) % n != 0):
        message += 'x'
    
    messageVectors = []

    i = 0
    while (i < len(message)):
        vector = []
        for _ in range(n):
            vector.append([getCode(message[i])])
            i += 1
        messageVectors.append(vector)
    
    # print(messageVectors)
    return messageVectors

def multiply(key: list, message: list, n: int) -> list:
    result = []

    resultMatrix = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(len(key)):
        for j in range(len(message[0])):
            for k in range(len(message)):
                resultMatrix[i][j] += key[i][k] * message[k][j]

    # print(resultMatrix)

    for i in range(n):
        x = resultMatrix[i][0]
        while (x > 26):
            x %= 26
        result.append(x)

    # print(result)
    return result


def encrypt(message: str, key: str, n: int) -> str:
    cipherText = ''
    messageVectors = getMessageVectors(message, n)
    keyMatrix = getKeyMatrix(key, n)

    resultVectors = []
    for msg in messageVectors:
        resultVectors.append(multiply(keyMatrix, msg, n))
    # print(resultVectors)

    for result in resultVectors:
        for r in result:
            cipherText += getChar(r)

    return cipherText

def decrypt(message: str, key: str, n: int) -> str:
    plainText = ''
    messageVectors = getMessageVectors(message, n)
    keyMatrix = np.array(getKeyMatrix(key, n))

    print(np.linalg.inv(keyMatrix))


    return plainText

if __name__ == '__main__':
    message = 'exam'.lower()
    key = 'hill'.lower()
    n = 2

    cipher = encrypt(message, key, n)
    print('Encryption:', cipher)

    message = decrypt(cipher, key, n)
    print('Decryption:', message)