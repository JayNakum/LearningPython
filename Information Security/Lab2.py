# PLAYFAIR CIPHER

def getKeyMatrix(key: str) -> list:
    keyMatrix = []

    ALPHA = 'abcdefghiklmnopqrstuvwxyz'
    keyList = []
    indexK = 0
    indexA = 0

    for _ in range((len(ALPHA) + len(key))):
        if(indexK < len(key)):
            if ((key[indexK].lower() not in keyList)):
                keyList.append(key[indexK])
            indexK += 1
        else:
            if ((ALPHA[indexA].lower() not in keyList)):
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

    return keyMatrix

def encrypt(key:str, message:str) -> str:
    cipher = ''
    keyMatrix = getKeyMatrix(key)
    plainText = []


    for i in range(0, len(message), 2):
        
        pair = message[i]
        if (message[i] == message[i + 1]):
            pair += 'x'
            i -= 1
        else:
            pair += message[i + 1]
        
        plainText.append(pair)
        # i += 1
            


    print(plainText)
    


if __name__ == "__main__":
    # message = input('Enter your message: ')
    # key = int(input('Enter key: '))
    message = 'moonmission'
    key = 'Engineering'

    # print(getKeyMatrix(key))
    encrypt(key, message)
    
