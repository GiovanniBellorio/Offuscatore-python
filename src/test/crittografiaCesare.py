#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Nome file: 20111011_01_Crittografia di Cesare.py
Descrizione: Algoritmo di crittografia secondo Cesare
'''

nome_programma= "20111011_01_Crittografia di Cesare.py"
print("Inizio esecuzione "+nome_programma)

scostamento=int(input("Inserisci uno scostamento: "))
messIn=input("Inserire un messaggio da criptare: ")
messOut=""
i=0
#Per migliorare l'efficenza scrivo il camando fuori dal ciclo
lenMessIn=len(messIn)

while i< lenMessIn:
    messOut= messOut+chr((ord(messIn[i])+scostamento)%256)
    i=i+1

print("Il messaggio criptato e': " + messOut)



print("Fine esecuzione")

    

