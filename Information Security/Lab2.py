# Experiment 2: Playfair Cipher

def getKeyMatrix(key: str) -> list:
    keyMatrix = []
    ALPHA = 'abcdefghiklmnopqrstuvwxyz'
    keyList = []
    indexK = 0
    indexA = 0

    for _ in range((len(ALPHA) + len(key))):
        if(indexK < len(key)):
            if (key[indexK].lower() not in keyList):
                keyList.append(key[indexK])
            indexK += 1
        else:
            if (ALPHA[indexA] not in keyList):
                keyList.append(ALPHA[indexA])
            indexA += 1

    count = 0
    row = []
    for char in keyList:
        row.append(char)
        count += 1
        if (count % 5 == 0):
            keyMatrix.append(row)
            row = []
    # print(keyMatrix)
    return keyMatrix

def getPosFromMatrix(char:str, matrix:list) -> tuple:
    for row in range(5):
        for col in range(5):
            if(char == matrix[row][col]):
                # print(row, col)
                return (row, col)

    return (-1, -1)


def getPairs(message:str) -> list:
    pairs = []
    
    i = 0
    while (i < len(message)):
        p1 = message[i]
        i += 1

        if (i == len(message)):
            p2 = 'x'
        else:
            p2 = message[i]
        
        if (p1 == p2):
            p2 = 'x'
        else:
            i += 1

        pair = p1 + p2
        pairs.append(pair)

    # print(pairs)
    return pairs

def encrypt(key:str, message:str) -> str:
    cipher = ''
    keyMatrix = getKeyMatrix(key)
    pairs = getPairs(message)
    
    for pair in pairs:        
        posP = getPosFromMatrix(pair[0], keyMatrix)
        posQ = getPosFromMatrix(pair[1], keyMatrix)

        if (posP[0] == posQ[0]):
            cipher += keyMatrix[posP[0]][(posP[1] + 1) % 5]
            cipher += keyMatrix[posQ[0]][(posQ[1] + 1) % 5]
        elif (posP[1] == posQ[1]):
            cipher += keyMatrix[(posP[0] + 1) % 5][posP[1]]
            cipher += keyMatrix[(posQ[0] + 1) % 5][posQ[1]]
        else:
            cipher += keyMatrix[posP[0]][posQ[1]]
            cipher += keyMatrix[posQ[0]][posP[1]]

    return cipher

def decrypt(key:str, cipher:str) -> str:
    message = ''
    keyMatrix = getKeyMatrix(key)
    pairs = getPairs(cipher)
    
    for pair in pairs:        
        posP = getPosFromMatrix(pair[0], keyMatrix)
        posQ = getPosFromMatrix(pair[1], keyMatrix)

        if (posP[0] == posQ[0]):
            message += keyMatrix[posP[0]][(posP[1] - 1) % 5]
            message += keyMatrix[posQ[0]][(posQ[1] - 1) % 5]
        elif (posP[1] == posQ[1]):
            message += keyMatrix[(posP[0] - 1) % 5][posP[1]]
            message += keyMatrix[(posQ[0] - 1) % 5][posQ[1]]
        else:
            message += keyMatrix[posP[0]][posQ[1]]
            message += keyMatrix[posQ[0]][posP[1]] 

    return message


if __name__ == "__main__":
    message = input('Enter your message: ')
    key = input('Enter key: ')

    cipher = encrypt(key, message)
    print(cipher)
    plaintext = decrypt(key, cipher)
    print(plaintext)
