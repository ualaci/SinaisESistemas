# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 20:00:27 2021

@author: Uálaci dos Anjos
"""

import numpy as np
from numpy import pi,cos,sin
from numpy.fft import fft, ifft, fftfreq, fftshift
import scipy as sp
import matplotlib.pyplot as plt

def plotaSinais(f1,f2,t,n,titulo,xLabel,yLabel,f1Label,f2Label,signalType,scale):
    fig, ax1 = plt.subplots()
    if (signalType == 1):        
        ax1.stem(t, f1, linefmt='r-',use_line_collection=True)
        ax1.stem(n, f2, linefmt='r-',use_line_collection=True)
    
    else: 
        ax1.plot(t, f1, 'red', linewidth=2, label = f1Label)
        ax1.plot(n, f2, 'green', linewidth=2, label = f2Label)
    
    scale_factor = scale

    xmin, xmax = plt.xlim()
    ymin, ymax = plt.ylim()
    
    plt.xlim(xmin * scale_factor, xmax * scale_factor)
    #plt.ylim(ymin * scale_factor, ymax * scale_factor)
    
    ax1.legend()
    ax1.axhline(y=0, color='k')
    ax1.axvline(x=0, color='k')
    ax1.set_xlabel(xLabel)
    ax1.set_ylabel(yLabel)
    ax1.grid(True)
    ax1.set_title(titulo)
    fig.tight_layout()
    plt.show()
    
def plotaSinal(f,t,titulo,xLabel,yLabel,signalType,scale):
    fig, ax1 = plt.subplots()
    if (signalType == 1):        
        ax1.stem(t, f, linefmt='blue',use_line_collection=False)
    
    else: 
        ax1.plot(t, f, 'blue', linewidth=2)

    scale_factor = scale

    xmin, xmax = plt.xlim()
    ymin, ymax = plt.ylim()
    
    plt.xlim(xmin * scale_factor, xmax * scale_factor)
    #plt.ylim(ymin * scale_factor, ymax * scale_factor)
    
    ax1.axhline(y=0, color='k')
    ax1.axvline(x=0, color='k')
    ax1.set_xlabel(xLabel)
    ax1.set_ylabel(yLabel)
    ax1.grid(True)
    ax1.set_title(titulo)
    fig.tight_layout()
    plt.show()

def fourierTransform(x, precisao, N):
    
    X = fft(x,N)/N
    w = fftfreq(len(X), precisao)*2*pi

    wDeslocado = fftshift(w)
    XDeslocado = fftshift(X)
    XModulo = abs(XDeslocado)

    return XModulo, wDeslocado
    
def main():
    w0 = 10
    precisao = 0.00001
    f1=1000
    f2=4000
    f3=6000
    
    t = np.arange(-1/f1, 1/f1,precisao)
    
    fAmostragem=5000
    fAmostragem2=12500
    precisao2 = 1/fAmostragem
    precisao3=1/(fAmostragem2)
    
    n=np.arange(-1/f1, 1/f1,precisao2)
    n2=np.arange(-1/f1, 1/f1,precisao3)
    
    #x2 corresponde ao sinal de entrada
    #x3 corresponde ao sinal de entrada amostrado com frequencia de amostragem de 12000, (xo(t) da letra B)
    #x4 corresponde ao sinal de entrada amostrado com frequencia de amostragem de 12000, (xo(t) da letra A)
    
    x2=2*sin(2*pi*f1*t)+2*sin(2*pi*f2*t)+sin(2*pi*f3*t)
    x3=2*sin(2*pi*f1*n2)+2*sin(2*pi*f2*n2)+sin(2*pi*f3*n2)
    x4=2*sin(2*pi*f1*n)+2*sin(2*pi*f2*n)+sin(2*pi*f3*n)
    
    N1 = int (len(x2))
    print(N1)
    N2 = len(x4)
    N3 = len(x3)
    print(N2)
    print(N3)
    
    X1, w1 = fourierTransform(x2, precisao, N1)
    X2, w2 = fourierTransform(x4, precisao2, N2)
    X3, w3 = fourierTransform(x3, precisao3, N3)

    # plotagem dos sinais
    plotaSinal(x2,t,"x(t)","x-Axis","y-Axis",0,1)
    plotaSinal(x4,n,"xo(t) Letra A","x-Axis","y-Axis",1,1)
    plotaSinal(x3,n2,"xo(t) Letra B","x-Axis","y-Axis",1,1)
    plotaSinal(X1,w1,"X1(jw)","xLabel","y-Axis",1,0.2)
    plotaSinal(X2,w2,"X2(jw)","xLabel","y-Axis",1,1)
    plotaSinal(X3,w3,"X3(jw)","xLabel","y-Axis",1,1)
    plotaSinais(x2,x4,t,n,"sinais x(t) continuo e amostrado sobrepostos","x-Axis","y-Axis","x(t)","xo(t)LetraA",0,1)
    plotaSinais(x2,x3,t,n2,"sinais x(t) continuo e amostrado sobrepostos","x-Axis","y-Axis","x1(t)","xo(t)LetraB",0,1)
    
main()