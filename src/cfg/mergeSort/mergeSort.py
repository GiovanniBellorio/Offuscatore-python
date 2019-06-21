from datetime import*
import random
#--DOC
'''
Nome programma: mergeSort.py
Descrizione: algoritmi
'''
nome_programma = "MergeSort.py"
print("Inizio esecuzione di " + nome_programma)

#-- FUNZIONI
'''
Nome funzione: creaVettore
Descrizione: creazione vettore casuale
Parametri: nElementi
'''
def creaLista(nElementi):
    vettore = []
    i = 0
    for i in range(0,nElementi):
        vettore.append(int(random.random()*100+1))
    return vettore

'''
Nome funzione: merge
Descrizione: fusione di due liste ordinate
Parametri: vettore
'''
def merge(l1, l2):
    l3 = []
    iDx1 = 0
    iDx2 = 0
    while iDx1 < len (l1) and iDx2< len (l2):
        if l1[iDx1] < l2[iDx2]:
            l3.append (l1[iDx1])
            iDx1 += 1
        else:   #if l1[iDx1] > l2[iDx2]:
            l3.append (l2[iDx2])
            iDx2 += 1
    while iDx1 < len(l1):
        l3.append (l1[iDx1])
        iDx1 += 1
    while iDx2 < len(l2):
        l3.append (l2[iDx2])
        iDx2 += 1
    return l3

'''
Nome funzione: mergeSort
Descrizione: 
Parametri: lista casuale
'''
def mergeSort(l):
    l2 = []
    l3 = []
    if len(l) > 1:
        mezzo = int (len(l)/2)
        #i = 0
        for i in range (0, mezzo):
            l2.append(l[i])
        for i in range (mezzo, len(l)):
            l3.append(l[i])
        v2 = mergeSort(l2)
        v3 = mergeSort(l3)
        lFin = merge (v2,v3)
        return lFin
    if len(l)==1:
        return l

#-- INPUT
boolDebug = True
if boolDebug == True:   #valori random
    elementi = int(input("Inserisci numero elementi vettore: "))
    lista = creaLista(elementi)
    lista1 = [3,5]
    lista2 = [7,12,15]
if boolDebug == False:  #valori fissi
    lista1 = [3,5]
    lista2 = [7,12,15]

#-- ELABORAZIONE
inizio=datetime.utcnow()
if __name__=="__main__":
    if boolDebug == True:
        print("Lista:      "  + str(lista))
        
    lista3 = merge(lista1, lista2)
    listaMerge = mergeSort (lista)
    

fine=datetime.utcnow()
#-- OUTPUT

print("MergeSort:  " + str(listaMerge))
print("")
print("Fusione di due liste ordinate:")
print("")
print("Lista1:     " + str(lista1))
print("Lista2:     " + str(lista2))
print("Merge:      " + str(lista3))

tempo=fine-inizio
print(tempo)
print("Esecuzione terminata")
