# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 13:14:55 2021

@author: Uálaci dos Anjos
"""

import numpy as np
from numpy import pi
from numpy.fft import *
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

def main():
    
    accuracy = 0.0001

# x[n] =  cos((6pi*n/13) + (π/6))
#W = Frequencia angular
#N = Periodo fundamental so sinal periodico

# Sinal item A
    N = 13
    countN = 2
    W = (6*pi)/13

    n = np.arange(0, countN*N)
    x = np.cos((W*n) + (pi/6))
    
    xFourier = fft(x)/len(x)
    xFourierShifted = fftshift(xFourier)
    
    f = fftfreq(len(n), 1/N)
    k = fftshift(f)

    moduleXFourier = np.abs(xFourierShifted)
    phaseXFourier = np.angle(xFourierShifted)
    phaseXFourier[moduleXFourier < accuracy] = 0
    
    
    plotaSinal(moduleXFourier,k,"|x[k]| 1-A","","Amplitude")
    plotaSinal(phaseXFourier,k,"Fase  1-A","","Amplitude")

    
# Sinal item B
# x[n] =  sen(4pi*n/21) + cos(10pi*n/21) + 1
#a funcao e derivada da soma de 3 outras funcoes portanto tera 3 frequencias angulares:
    
    N = 21
    countN = 2
    W1 = (4*pi)/N
    W2 = (10*pi)/N
    W3 = 1
    

    n = np.arange(0, countN*N)
    x = np.sin(W1*n) + np.cos(W2*n) + 1
    
    xFourier = fft(x)/len(x)
    xFourierShifted = fftshift(xFourier)
    
    f = fftfreq(len(n), 1/N)
    k = fftshift(f)
    
    

    moduleXFourier = np.abs(xFourierShifted)
    phaseXFourier = np.angle(xFourierShifted)
    phaseXFourier[moduleXFourier < accuracy] = 0
    

    plotaSinal(moduleXFourier,k,"|x[k]| 1-B","","Amplitude")
    plotaSinal(phaseXFourier,k,"Fase 1-B","","Amplitude")

# Sinal item C
    N = 8
    countN = 3
    n = np.arange(0, (countN*N), 1)
    
    x = np.zeros(len(n))
    j = 1
    i = 3
    
    while(i < len(n)):
       x[i] = (-1)**j
       i = i+4
       j = j+1
    
    xFourier = fft(x)/len(x)
    f = fftfreq(len(n), 1/N)
    xFourierShifted = fftshift(xFourier)           
    k = fftshift(f)
    moduleXFourier = np.abs(xFourierShifted)
    phaseXFourier = np.angle(xFourierShifted)
    phaseXFourier[moduleXFourier < accuracy] = 0
    
    
    plotaSinal(moduleXFourier,k,"|x[k]| 1-C","","Amplitude")
    plotaSinal(phaseXFourier,k,"Fase 1-C","","Amplitude")
    
# Sinal item D
    N = 5
    countN = 4
    n = np.arange(0, (countN*N), 1)
    x = []
    j = 0
    
    for i in range(len(n)):
        x.append(j*0.25)
        j = j+1
        
        if(j == N):
            j = 0
    
    xFourier = fft(x)/len(x)
    xFourierShifted = fftshift(xFourier)
    
    f = fftfreq(len(n), 1/N)
    k = fftshift(f)
    
    moduleXFourier = np.abs(xFourierShifted)
    phaseXFourier = np.angle(xFourierShifted)
    phaseXFourier[moduleXFourier < accuracy] = 0
    
    plotaSinal(moduleXFourier,k,"|x[k]| 1-D","","Amplitude")
    plotaSinal(phaseXFourier,k,"Fase 1-D","","Amplitude")


# Sinal item E
    N = 9
    countN = 3
    
    n = np.arange(0, (countN*N), 1)
    x = np.zeros(len(n))
    j = 0
    
    for i in range(len(n)):
        if(n[i] % N != 0):
            if(j < 4):    
                x[i] = 1
                
            elif(j > 3 and j < N):
                x[i] = -1
            j = j+1
            
        else:
            j = 0
        
    xFourier = fft(x)/len(x)
    xFourierShifted = fftshift(xFourier)
    
    f = fftfreq(len(n), 1/N)
    k = fftshift(f)
    
    moduleXFourier = np.abs(xFourierShifted)
    phaseXFourier = np.angle(xFourierShifted) 
    phaseXFourier[moduleXFourier < accuracy] = 0
    
    plotaSinal(moduleXFourier,k,"|x[k]| 1-E","","Amplitude")
    plotaSinal(phaseXFourier,k,"Fase 1-E","","Amplitude")

    
main()