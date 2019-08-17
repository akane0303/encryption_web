def encrypt(text, key):
    text = text.upper()
    key = key.upper()
    cipher = ''
    for i in range(len(text)):
        t = text[i]
        k = key[i%len(key)]
        n = (ord(t)+ord(k)-130) % 26
        cipher += chr(n+65)
    return cipher
 
def decrypt(cipher, key):
    cipher = cipher.upper()
    key = key.upper()
    text = ''
    for i in range(len(cipher)):
        c = cipher[i]
        k = key[i%len(key)]
        n = (26-ord(k)+ord(c)) % 26
        text += chr(n+65)
    return text
 
if(__name__ == '__main__'):
    import sys
    text = "doyoulikemisosiru"
    key = "hello"
    cipher = encrypt(text, key)
    print(cipher)
    text = decrypt(cipher, key)
    print(text)
