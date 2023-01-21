import math
import random

def getNum(char:str) -> int:
    if (char.islower()):
        return ((ord(char) - ord('a')) % 26) + 1
    if (char.isupper()):
        return ((ord(char) - ord('A')) % 26) + 1

def getChar(num:int) -> str:
    return chr(((num % 26) + 65) - 1) 


def isCoprime(x: int, y: int) -> bool:
    return math.gcd(x, y) == 1

def getPublicKey() -> int:
    cofactors = []

    for i in range(2, tN):
        if(isCoprime(i, tN)):
            cofactors.append(i)
    # print(cofactors)

    e = random.choice(cofactors)
    # print(e)

    return e

def getPrivateKey(e:int) -> int:
    return pow(e, -1, tN)

def encrypt(M, e) -> int:
    return pow(M, e, n)

def decrypt(C, d) -> int:
    return pow(C, d, n)


if __name__ == "__main__":
p = 7
q = 19
n = p * q
tN = (p-1) * (q-1)
e = getPublicKey()
d = getPrivateKey(e)
message = "abcde"
cipher = []
for ch in message:
    cipher.append(encrypt(getNum(ch), e))
# print(cipher)
    
original = ""
for ch in cipher:
    print(getChar(ch))
    original += getChar(decrypt(ch, d))
print(original)
