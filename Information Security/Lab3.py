# Rail Fence Cipher

def encrypt(plainText: str) -> str:
    cipher = ''
    matrix = [['_' for i in range(len(plainText))]
                  for j in range(2)]
    i = 0
    altIndex = 0
    for char in plainText:
        matrix[altIndex][i] = char
        i += 1
        if (altIndex):
            altIndex = 0
        else:
            altIndex = 1
    
    # print(matrix)

    for row in matrix:
        for char in row:
            if(char == '_'): continue
            cipher += char

    return cipher

def decrypt(cipher: str) -> str:
    matrix = []
    tmpString = []

    alternateFlg = True
    i = 0
    count = 0
    while (i < len(cipher)):

        if (count == len(cipher)):
            matrix.append(tmpString)
            tmpString = []
            alternateFlg = False

        if (alternateFlg):
            tmpString.append(cipher[i])
            i += 1
        else :
            tmpString.append('_')

        alternateFlg = not alternateFlg
        count += 1

    matrix.append(tmpString)
    
    # print(matrix)

    plainText = ''
    index = 0
    altIndex = 0
    for _ in range(len(cipher)):
        plainText += matrix[altIndex][index]

        if (altIndex):
            altIndex = 0
        else:
            altIndex = 1
        
        index += 1

    return plainText


if __name__ == "__main__":
    # message = input('Enter your message: ')
    message = 'JayNakum'

    cipher = encrypt(message)
    print(cipher)

    plainText = decrypt(cipher)
    print(plainText)