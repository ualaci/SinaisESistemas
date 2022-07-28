# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 14:20:01 2021

@author: Uálaci dos Anjos
"""

import numpy as np
from numpy import pi
from numpy.fft import *
import scipy as sp
import matplotlib.pyplot as plt

def plotaSinal(f,t,titulo,xLabel,yLabel):
    fig, ax1 = plt.subplots()
    ax1.stem(t, f, linefmt='r-',use_line_collection=True)
    #ax1.plot(t, f, 'c-', linewidth=2)
    ax1.axhline(y=0, color='k')
    ax1.axvline(x=0, color='k')
    ax1.set_xlabel(xLabel)
    ax1.set_ylabel(yLabel)
    ax1.grid(True)
    ax1.set_title(titulo)
    fig.tight_layout()
    plt.show()
    
    #W = Frequencia angular
    #N = Periodo fundamental do sinal periodico
    #K = Periodo fundamental de x[k]
    #countK = quantidade de periodos

def main():
# sinal item A:
    K = 17
    countK = 1
    W = (6*pi)/17

    k = np.arange(0, countK*K)
    xFourier = np.cos(W*k)
    x = ifft(xFourier)*len(k)
    x = np.real(x)   
    n=fftfreq(len(k), 1/K)
    
    
    plotaSinal(xFourier,k,"Dominio da frequencia: x[k] 2-A","","Amplitude")
    plotaSinal(x,n,"Dominio do tempo: x[n] 2-A","","Amplitude")


# sinal item B:
    K = 21
    countK = 2
    
    W1 = (10*pi)/21
    W2 = (4*pi)/21

    k = np.arange(0, countK*K)
    xFourier = []
    
    for i in range(len(k)):
        a = np.cos(W1 * k[i])
        b = np.cos(W2 * k[i])
        xFourier.append(complex(a, b))

    realOfX = []
    
    for i in range(len(xFourier)):
        realOfX.append(xFourier[i].real)
     
    x = ifft(xFourier) * len(k) 
    x = np.real(x)
    n=fftfreq(len(k), 1/K) 
    
    plotaSinal(realOfX,k,"Dominio da frequencia: x[k] 2-B","","Amplitude")
    plotaSinal(x,n,"Dominio do tempo: x[n] 2-B","","Amplitude")


# sinal item C:
    K = 7
    countK = 2

    k = np.arange(countK*(-1)*K, countK*K)
    xFourier = np.zeros(len(k))
    j = 2
    
    for i in range(len(k)):
        if(j >= 5 and j <= 6):
            xFourier[i] = 1
        j = j+1
        
        if(j > 6):
            j = 0
       
    x = ifft(xFourier)*len(k)          
    x = np.real(x)
    n = np.arange(0, len(k))
    n=fftfreq(len(k), 1/K) 
    
    plotaSinal(xFourier,k,"Dominio da frequencia: x[k] 2-C","","Amplitude")
    plotaSinal(x,n,"Dominio do tempo: x[n] 2-C","","Amplitude")


# sinal item D:
    K = 7
    countK = 2

    k = np.arange(countK*(-1)*K, countK*K)

    xFourier = np.zeros(len(k))
    j = 0
    
    for i in range(len(k)):
        if(k[i] % 7 == 0):
            xFourier[i] = -1/2
        else:
            if(j == 0):
                xFourier[i] = 1
                
            if(j == 5):
                xFourier[i] = 1
                
            j = j+1
            
        if(j == 6):
            j = 0
 
    x = ifft(xFourier)*len(k)          
    x = np.real(x)
    n = np.arange(0, len(k))

    plotaSinal(xFourier,k,"Dominio da frequencia: x[k] 2-D","","Amplitude")
    plotaSinal(x,n,"Dominio do tempo: x[n] 2-D","","Amplitude")
    

main()


