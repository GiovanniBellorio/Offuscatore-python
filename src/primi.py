#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Nome file:Il crivello di eratostele.py
Descrizione: questo programma genera i numeri primi
inferiori ad un numero dato"
'''

nome_programma="Il crivello di eratostele.py"
print("Inizio esecuzione " + nome_programma)

n=int(input("Numeri primi inferiori ad n (n maggiore di 2): "))
listaprimi=[]
for i in range(2,n):        # analizzo tutti i numeri i tra 2 ed n
    primo=True              # controllo se i e' primo
    for j in range(2,i):
        if i%j==0:
            primo=False     # i non e' primo
    if primo:               # i e' primo, quindi lo aggiungo alla lista dei primi
            listaprimi.append(i)

print("I numeri primi inferiori a " + str(n) + " sono:")
print(listaprimi)
    
print("Fine esecuzione")
