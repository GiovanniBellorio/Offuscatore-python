#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Nome file: 20111011_01_Decriptare.py
Descrizione: Algoritmo per decriptare un messaggio criptato
'''

nome_programma= "Decriptare.py"
print("Inizio esecuzione " + nome_programma)

s=1
messOut=input("Inserire un messaggio criptato: ")
messIn=""
i=0
lenMessOut=len(messOut)

while s<256:
    while i<lenMessOut:
        messIn=messIn+chr((ord(messOut[i])-s)%256)
        i=i+1
    messIn += "\n"
    i=0
    s=s+1
print("Il messaggio decriptato e': " + messIn)
    
    
print("Fine esecuzione")

    

