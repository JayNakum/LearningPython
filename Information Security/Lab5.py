# Lab 5 and 6
# Experiment 6: Hill Cipher

import numpy
from numpy import matrix
from numpy import linalg

def getChar(code: int) -> str:
    return chr(code % 26 + 97)


def getCode(char: str) -> int:
    return (ord(char) - 97) % 26


def modInverse(a: int, m: int) -> int:
    a %= m
    for x in range(m):
        if ((a * x) % m == 1):
            return x
    return 1


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

def moduloInverse(det):
    for i in range(1, 26, 1):
        if (i*det) % 26 == 1:
            return i

def getInverseKeyMatrix(key_matrix):
    det = numpy.linalg.det(key_matrix)
    adj = numpy.linalg.inv(key_matrix)*det
    adj = adj.astype(int)

    det = det % 26
    det = round(det)
    det = moduloInverse(det)
    
    inv = adj*det
    inv = inv % 26

    return inv

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


def encrypt(message: str, key: str, n: int) -> str:
    cipherText = ''
    messageVectors = getMessageVectors(message, n)
    keyMatrix = getKeyMatrix(key, n)

    resultVectors = []
    for vector in messageVectors:
        resultVectors.append(multiply(keyMatrix, vector, n))
    # print(resultVectors)

    for result in resultVectors:
        for r in result:
            cipherText += getChar(r)

    # print(cipherText)
    return cipherText

def decrypt(message: str, key: str, n: int) -> str:
    messageVectors = getMessageVectors(message, n)
    keyMatrix = getKeyMatrix(key, n)
    inverseKeyMatrix = getInverseKeyMatrix(numpy.array(keyMatrix))

    plainText = ""
    resultVectors = []
    for vector in messageVectors:
        resultVectors.append(multiply(inverseKeyMatrix, vector, n))
    
    # print(resultVectors)
    for result in resultVectors:
        for r in result:
            plainText += getChar(int(r))

    return plainText


if __name__ == '__main__':
    message = 'abcdefghi'.lower()
    key = 'hillciphe'.lower()
    n = 3

    cipher = encrypt(message, key, n)
    print('Encryption:', cipher)

    message = decrypt(cipher, key, n)
    print('Decryption:', message)
