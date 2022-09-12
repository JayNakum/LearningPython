# Double Transposition

def encrypt(plainText: str, key: str) -> str :
    matrix = []
    i = 0
    canExit = False
    for _ in plainText:
        if (canExit): break;
        row = []
        for _ in key:
            if (i >= len(plainText)): 
                row.append('X')
                canExit = True
            else:
                row.append(plainText[i])
                i += 1
        if (row != []) :
            matrix.append(row)

    # print(matrix)

    kpt = {}
    i = 0
    for k in key:
        kpt[int(k)] = [row[i] for row in matrix]
        i += 1

    cipher = ''
    for i in range(len(kpt)):
        for j in range(len(kpt[i+1])):
            cipher += kpt[i+1][j]

    return cipher

def decrypt(plainText: str, key:str) -> str:
    matrix = []
    i = 0
    for char in plainText:
        row = []
        for _ in range(len(plainText) // len(key)):
            if (i >= len(plainText)): 
                row.append('X')
                continue
            else:
                row.append(plainText[i])
                i += 1
        if (row != []):
            matrix.append(row)

    # print(matrix)

    plainText = ''
    for i in range(len(matrix[0])):
        for k in key:
            plainText += matrix[int(k) - 1][i]

    return plainText

if __name__ == "__main__":
    # message = input('Enter your message: ')
    # key = input('Enter your key: ')
    message = 'attackpostponeduntiltwoam'
    key ='4312567'
    key2 ='7652134'

    cipher = encrypt(message, key)
    print(cipher)

    cipher2 = encrypt(cipher, key2)
    print(cipher2)

    plainText = decrypt(cipher2, key2)
    pt = ''
    for i in range(len(cipher)):
        pt += plainText[i]
    print(pt)

    plainText2 = decrypt(pt, key)
    print(plainText2)
