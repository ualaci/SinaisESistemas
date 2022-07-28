# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 20:10:37 2021

@author: Uálaci dos Anjos
"""
import numpy as np

def E1(s, n):
    size = len(s)
    sReverso = [0]*size
    nReverso = [0]*size
    
    for x in range (0,size):
        sReverso[size-x-1]=s[x]
        nReverso[size-x-1]=n[x]*(-1)
    
    sPar = []
    sImpar = []
    
    sizeSPar = max(s[size-1],sReverso[size-1]) - min(s[0],sReverso[0])
    
    n2 = []
    n2 = nReverso.copy()
    
    for x in range (0,size):
        if n[x] not in n2:
            n2.append(n[x])
    n2.sort()
    
    print("n2",n2)
    
    for x in range (0,len(n2)):
        
        if n2[x] in n :
            if n2[x] in nReverso:
                indexN = n.index(n2[x])
                indexNReverso = nReverso.index(n2[x])
                sPar.append((s[indexN] + sReverso[indexNReverso])/2)
                sImpar.append((s[indexN] - sReverso[indexNReverso])/2)
                
        if n2[x] in n:
            if n2[x] not in nReverso:
                index = n.index(n2[x])
                sPar.append(s[index]/2)
                sImpar.append(s[index] /2)
        
        if n2[x] in nReverso:
            if n2[x] not in n:
                index = nReverso.index(n2[x])
                sPar.append(sReverso[index]/2)
                sImpar.append(-sReverso[index]/2)
            
    print("P", sPar)
    print("I", sImpar)


def main():
    print("funcao 1")
    E1 ([ 2, 1, 0, 1, 2],[-2, -1, 0, 1, 2])
    print("funcao 2")
    E1 ([-2,-1, 0, 1, 2],[-2, -1, 0, 1, 2])
    print("funcao 3")
    E1 ([ 0, 0 ,0 , 2, 4],[-2, -1, 0, 1, 2])
    print("funcao 4")
    E1 ([ 0 , -1 , -1, 3 , 2], [-2, -1, 0, 1, 2])
    print("funcao 5")
    E1 ([ 0, 0 ,0 , 2, 4], [ 0, 1, 2, 3, 4])
    
    