# CAESER CIPHER

def encrypt(key: int, message: str) -> str:
    
    cipher = ""
    
    for i in range(len(message)):
        
        if(message[i] == ' '):
            cipher += ' '
        else:

            if(message[i].isdigit()):
                cipher += str(int(message[i]) + key)
            else:
                if (message[i].islower()):
                    ascii = ord(message[i]) - 97
                else:
                    ascii = ord(message[i]) - 65

                ##########################
                ascii = (ascii + key) % 26
                ##########################
                
                if (message[i].islower()):
                    cipher += chr(ascii + 97)
                else:
                    cipher += chr(ascii + 65)
            
    return cipher

def decrypt(key: int, cipher: str) -> str:
    message = ""
    
    for i in range(len(cipher)):
        
        if(cipher[i] == ' '):
            message += ' '
        else:

            if(cipher[i].isdigit()):
                message += str(int(cipher[i]) - key)
            else:
                if (cipher[i].islower()):
                    ascii = ord(cipher[i]) - 97
                else:
                    ascii = ord(cipher[i]) - 65

                ##########################
                ascii = (ascii - key) % 26
                ##########################
                
                if (cipher[i].islower()):
                    message += chr(ascii + 97)
                else:
                    message += chr(ascii + 65)
            
    return message

if __name__ == "__main__":
    message = input('Enter your message: ')
    key = int(input('Enter key: '))

    cipher = encrypt(key, message)
    print(cipher)
    
    plainText = decrypt(key, cipher)
    print(plainText)
