# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 19:42:32 2021

@author: Uálaci dos Anjos
"""

import numpy as np
from numpy import pi
from numpy.fft import *
import scipy as sp
import matplotlib.pyplot as plt
from scipy import signal

def sawTooth(wt):
    x = sp.signal.sawtooth(wt, 1) * 3/4 + 1/4
    return x

def plotaSinal(f,t,titulo,xLabel,yLabel,signalType):
    fig, ax1 = plt.subplots()
    if (signalType == 1):        
        ax1.stem(t, f, linefmt='r-',use_line_collection=True)
    
    else: 
        ax1.plot(t, f, 'c-', linewidth=2)
        
    ax1.axhline(y=0, color='k')
    ax1.axvline(x=0, color='k')
    ax1.set_xlabel(xLabel)
    ax1.set_ylabel(yLabel)
    ax1.grid(True)
    ax1.set_title(titulo)
    fig.tight_layout()
    plt.show()


def main():
    #f = frequencia
    #T = Periodo
    #size = tamanho da amostragem
    #w0 = frequencia angular
    
    accuracy = 0.0001
    T = 3/2
    f = 1/T
    size = T*0.01
    w0 = 2*pi*f

    t = np.arange(-3, 2*T, size)
    x = sawTooth(w0*t)
    
    xFourier = fft(x)/len(x)
    xFourierShifted = fftshift(xFourier)
    
    w = fftfreq(len(t), f*size)
    wShifted = fftshift(w)

    moduleXFourier = np.abs(xFourierShifted)
    phaseXFourier = np.angle(xFourierShifted)

    xReal = ifft(xFourier)*len(x)
    xReal = np.real(xReal)
    phaseXFourier[moduleXFourier < accuracy] = 0
    
    plotaSinal(x,t,"x(t) original","tempo (s)","Amplitude",0)
    plotaSinal(moduleXFourier,wShifted,"|x[k]|","frequencia","Amplitude",1)
    plotaSinal(phaseXFourier,wShifted,"fase de x[k]","frequencia","Amplitude",1)

main()