# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 15:19:46 2021

@author: Uálaci dos Anjos
"""

import numpy as np
from numpy import pi,cos,sin
from numpy.fft import fft, ifft, fftfreq, fftshift
import scipy as sp
import matplotlib.pyplot as plt

def plotaSinal(f,t,titulo,xLabel,yLabel,signalType,scale):
    fig, ax1 = plt.subplots()
    if (signalType == 1):        
        ax1.stem(t, f, linefmt='r-',use_line_collection=True)
    
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


def fX(precisao,t2):
    #_____________________________________Rampa1___________________
    
    rampa1=[]
    
    i=-10
    j=0
    
    while(i<-5):
        rampa1.append(0)
        i=i+precisao
        
    i=-5
    
    while i<=10:
        rampa1.append(t2[j])
        j+=1
        i=i+precisao
        
        
    #_____________________________________Rampa2___________________:
        
    i=-10
    j=0
    rampa2=[]
    
    while(i<0):
        rampa2.append(0)
        i=i+precisao
        
    i=0
    
    while i<=10:
        rampa2.append(t2[j])
        j+=1
        i=i+precisao
        
    #_____________________________________Rampa3___________________
    
    rampa3=[]
    
    i=-10
    j=0
    
    while(i<5):
        rampa3.append(0)
        i=i+precisao
        
    i=5
    
    while i<=10:
        rampa3.append(t2[j])
        j+=1
        i=i+precisao
        
    #sinal x(t)
    x=[]
    i=-10
    j=0
    
    while(i<=10):
        x.append(0.2*(rampa1[j]-2*rampa2[j]+rampa3[j]))
        i=i+precisao
        j=j+1
    
    return x

def fourierTransform(x, precisao, N):
    
    X = (precisao*N)*fft(x,N)/N
    w = fftfreq(len(X), precisao)*2*pi

    wDeslocado = fftshift(w)
    XDeslocado = fftshift(X)
    XModulo = np.abs(XDeslocado)

    return XModulo, wDeslocado
    
def main():
    w0 = 10
    precisao = (2*pi)/(w0*100)
    N = 2**20
    t = np.arange(-10, 10,precisao)
    t2 = np.arange(0,30,precisao)
    
    x=fX(precisao,t2)
    X, wx = fourierTransform(x, precisao, N)
    
    p = cos(10*t)
    y = x*p
    Y, wy = fourierTransform(y, precisao, N)

    # plotagem dos sinais
    plotaSinal(x,t,"x(t)","x-Axis","y-Axis",0,1)
    plotaSinal(X,wx,"X(jw)","xLabel","y-Axis",0,0.025)
    plotaSinal(y,t,"y(t)","x-Axis","y-Axis",0,1)
    plotaSinal(Y,wy,"Y(jw)","x-Axis","y-Axis",0,0.025)
    
main()

    
