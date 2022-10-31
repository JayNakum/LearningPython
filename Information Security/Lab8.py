# RSA Algorithm
# Experiment 9

import random
import math
p = 7
q = 19
M = 6

def is_coprime(x, y):
    return math.gcd(x,y) == 1

def getE():
    cofactors = []

    for i in range(2,toitentOF_n):
        if(is_coprime(i,toitentOF_n)):
            cofactors.append(i)
            
    # print(cofactors)
    e = random.choice(cofactors)
    # print(e)
    return e

def getD():
    d=pow(e, -1, toitentOF_n)
    # print(d)
    return d

def encryption(M,d,n):
    return pow(M,d)%n

def decryption(encrypted,e,n):
    return pow(encrypted,e)%n

if __name__ == "__main__":
    n = p * q
    toitentOF_n = (p-1)*(q-1)
    
    e = getE()
    d = getD()
    encrypt_text = encryption(M,d,n)
    print("Digital Key :",encrypt_text)
    decrypt_text = decryption(encrypt_text,e,n)
    print("M1 :",decrypt_text)
    print("M :", M)
