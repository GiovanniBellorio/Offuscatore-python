#!/usr/bin/python
# -*- coding: utf-8 -*-

import couchdb
import math
from operator import itemgetter
from datetime import *

__server    = "127.0.0.1"
__dbName    = 'db_airlines'
__db4Log    = 'admin'
__user      = 'admin'
__pw        = 'Univr_2019'
__db4LogCon = None

def __cursor():
    """ Ritorna un cursore per scrivere nel database cls.__db4Log. """
    if __dbName in __db4LogCon:
        __db = __db4LogCon[__dbName]
        return __db

def tempo():
    return datetime.utcnow()

def Q5_airline():
    """ """
    cur = __cursor()
    doc = {} # "scode:dcode":count

    for item in cur.view('_design/documenti-view/_view/view_Q5', limit=3000000):
        scode = item.value[0]
        dcode = item.value[1]
        code  = scode + ":" + dcode

        if code in doc:
            count = doc[code]
            count += 1
            doc[code] = count
        else:
            doc[code] = 1

    for item in cur.view('_design/documenti-view/_view/view_Q5', skip=3000000):
        scode = item.value[0]
        dcode = item.value[1]
        code  = scode + ":" + dcode

        if code in doc:
            count = doc[code]
            count += 1
            doc[code] = count
        else:
            doc[code] = 1
    
    doc_list = sorted(doc.items(), key=itemgetter(0))

    for c in doc_list:
        tmp = c[0].split(":")
        c1 = tmp[0]
        c2 = tmp[1]
        print((c1,c2), c[1])

    return 0


def main():
    print("INIZIO ESECUZIONE")
    print("--------------------------------------------------------------------------------")
    inizio = tempo()

    global __db4LogCon
    __db4LogCon = couchdb.Server("http://%s:%s@%s:5984/" % (__user, __pw, __server))

    Q5_airline()

    __db4LogCon = None

    fine = tempo()
    tempoImpiegato = fine - inizio
    print(tempoImpiegato)
    print("FINE ESECUZIONE")
    print("--------------------------------------------------------------------------------")


if __name__ == '__main__':
    main()