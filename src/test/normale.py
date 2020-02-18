#!/usr/bin/python
# -*- coding: utf-8 -*-

#from __future__ import division
import math
import random

import time
START  = time.time()

#-- DOC

#Autore:         Bellorio Giovanni
#Descrizione:    --Parte1--
#                Utilizzando i metodi integrazione numerica studiati,
#                tabulare la funzione che descrive le aree sottese alla
#                normale standardizzata da 0 a Z, con Z<=4.
#
#                --Parte2--
#                Utilizzando poi il metodo monte carlo e considerando un
#                particolare valore di Z, determinare l'area sottesa alla
#                funzione di densita' da 0 a Z e studiare la distribuzione
#                dei valori ottenuti per tale area al variare del numero
#                n di punti utilizzati per la simulazione.

#-- FUNZIONI
def calcolaNormale(n):
    result = (1/(math.sqrt(2*math.pi)))*math.pow(math.e, (-1/2)*math.pow(n,2))
    return result

#-- INPUT e VARIABILI
programName = "Tabella Normale"

i = 0.00
h = 0.01
simpson = 0.00
lista   = []

#-- ELABORAZIONE
if __name__=="__main__":
    print("Inizio elaborazione di " + programName)

    #-- I Parte
    while i<=4:
        a = calcolaNormale(i)
        b = calcolaNormale(i+0.005)
        c = calcolaNormale(i+0.01)
        simpson += (h/6)*(a+4*b+c)
    
        lista.append(simpson)
        #print i," ",simpson
        i += 0.01

    #-- II parte
    #z = int(input("Inserisci valore (0<=Z<=4): "))
    z = 1
    nRip  = 100000
    count = 0
    i     = 0
    sqrN  = 1/(math.sqrt(2*math.pi))
    while i < nRip:
        #range: 0_Z
        x = random.uniform(0,z)
        #range: 0_(1/sqrt2pi)
        y = random.uniform(0,sqrN)
        if (y <= calcolaNormale(x)):
            count += 1
        i += 1
    #print x, " ",y, " ",count
    print((count/nRip)*z*sqrN)

#-- OUTPUT
    print(lista)
    #print z
print("Fine elaborazione")

END = time.time() - START
print("Time: ", END)
