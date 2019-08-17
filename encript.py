#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse
def Encrypt(plaintext,key):
    plaintext=plaintext.upper()
    key=key.upper()
    chipher=''
    #while(len(plaintext)>len(key)):
    #plaintext+=plaintext
    for i in range(len(plaintext)):
        t=plaintext[i]
        k=key[i]
        numt=ord(t)-65
        numk=ord(k)-65
        print(numk)

        if((numt+numk)>25):
            code=(numt+numk)-26
        else:
            code=numt+numk
        print(code)
        chipher +=chr(code+65)
    return chipher

if __name__=='__main__':
    
    parser=argparse.ArgumentParser(description='暗号化します')
    parser.add_argument('message1',help='暗号化したい文を入力してください')
    parser.add_argument('message2',help='鍵を入力してね')
    message=sys.argv
    text=message[1]
    key=message[2]
    if len(message[1])>len(message[2]):
        print('Error:','your key is too small...I can not lock your secret')
    else:
        result=Encrypt(text,key)
        print('Not to worry,I keep a secret!')
        print('result:',result)

