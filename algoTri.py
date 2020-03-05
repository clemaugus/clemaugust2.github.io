import random
import time
from matplotlib.pyplot import *

maxVal = 2000
nVal = 1000
listeNombres = list(range(0,24,2))sorted(random.choices(range(maxVal),k=nVal))

def rechercheNaive(L: list, elt: int)-> int:
    for i in range(len(L)):
        #print("position ",i, " valeur ",L[i],elt)
        if elt == L[i]:
            return i
    return -1


def rechercheDicho(L: list, elt: int)-> int:
    tr = False
    deb = 0
    fin = len(L)-1
    cnt = 0
    while tr == False and deb <= fin:
        mil = (deb+fin) // 2
        #print(L[deb:fin+1])
        if L[mil] == elt:
            tr = True
        else :
            if elt > L[mil] :
                deb = mil+1
            else :
                fin = mil-1
        cnt += 1
    return cnt

listeNombres = sorted(random.choices(range(maxVal),k=nVal))
#print(rechercheDicho(listeNombres, 11))

#print(rechercheNaive(listeNombres,12))