# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 19:22:09 2021

@author: Uálaci dos Anjos
"""

import numpy as np
from numpy import pi,exp,cos,sin,abs
import scipy as sp
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft, fftfreq, fftshift

def plotaSinal(f,t,titulo,xLabel,yLabel,fLabel,color,signalType,scale):
    fig, ax1 = plt.subplots()
    if (signalType == 1):        
        ax1.stem(t, f, linefmt='r-',use_line_collection=True, label = fLabel)
    
    else: 
        ax1.plot(t, f, color, linewidth=2, label = fLabel)

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
    
def plotaSinais(f1,f2,f3,t,titulo,xLabel,yLabel,f1Label,f2Label,f3Label,signalType,scale):
    fig, ax1 = plt.subplots()
    if (signalType == 1):        
        ax1.stem(t, f1, linefmt='r-',use_line_collection=True)
        ax1.stem(t, f2, linefmt='r-',use_line_collection=True)
        ax1.stem(t, f3, linefmt='r-',use_line_collection=True)
    
    else: 
        ax1.plot(t, f1, 'red', linewidth=2, label = f1Label)
        ax1.plot(t, f2, 'green', linewidth=2, label = f2Label)
        ax1.plot(t, f3, 'blue', linewidth=2, label = f3Label)
    
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
    
def fourierTransform(x, precisao, N):
    
    X = (precisao*N)*fft(x,N)/N
    w = fftfreq(len(X), precisao)*2*pi

    wDeslocado = fftshift(w)
    XDeslocado = fftshift(X)
    XModulo = abs(XDeslocado)
    fase = np.angle(XDeslocado)
    return XModulo, fase,wDeslocado
    
def main():
    w1 = 7.5
    precisao = (2*pi)/(w1*100)
    N1 = 2**15
    t1 = np.arange(-10, 10,precisao)

    w2 = 60
    precisao = (2*pi)/(w2*100)
    t2 = np.arange(-0.5, 0.5,precisao)

    
    x1LetraA = np.zeros(len(t1))
    x2LetraA = np.zeros(len(t1))
    x3LetraA = np.zeros(len(t1))
    
    x1LetraA[np.logical_and(t1 >= 0, t1 <= 2)]=1
    
    x2LetraA[np.logical_and(t1 >= 0, t1 <= 1)]=1
    
    x3LetraA[np.logical_and(t1 >= 0, t1 <= 0.35)]=1
    
    X1LetraA, fase1LetraA, wLetraA = fourierTransform(x1LetraA, precisao, N1)
    X2LetraA, fase2LetraA, wLetraA = fourierTransform(x2LetraA, precisao, N1)
    X3LetraA, fase3LetraA, wLetraA = fourierTransform(x3LetraA, precisao, N1)

    xLetraB = exp(-1*abs(t1))
    xLetraB[t1<0]=0
    XLetraB, faseLetraB, wLetraB = fourierTransform(xLetraB, precisao, N1)

    xLetraC = sin(350*t2)
    XLetraC, faseLetraC, wLetraC = fourierTransform(xLetraC, precisao, N1)
    
    xLetraD = []
    w3=20
    precisao = precisao = (2*pi)/(w3*100)
    
    t3=np.arange(-31,31,precisao)
    
    j=0
    i=-31
    
    while(i<=31):
        
        if(i%10<=0.005):
            xLetraD.append(1)
        else:
            xLetraD.append(0)
            
        i=i+precisao
        
    XLetraD, faseLetraD, wLetraD = fourierTransform(xLetraD, precisao, N1)

    # plotagem dos sinais
    plotaSinais(x1LetraA,x2LetraA,x3LetraA,t1,"sinais x(t) letra A","x-Axis","y-Axis","x1(t)","x2(t)","x3(t)",0,1)
    plotaSinais(X1LetraA,X2LetraA,X3LetraA,wLetraA,"sinais X(jw) letra A","x-Axis","y-Axis","X1(jw)","X2(jw)","X3(jw)",0,0.18)
    plotaSinais(fase1LetraA,fase2LetraA,fase3LetraA,wLetraA,"fases letra A","x-Axis","y-Axis","fase1", "fase2", "fase3",0,0.01)

    plotaSinal(xLetraB,t1,"x(t) Letra B","x-Axis","y-Axis","x(t)","blue",0,1)
    plotaSinal(XLetraB,wLetraB,"X(jw) Letra B","x-Axis","y-Axis","X(jw)","red",0,0.15)
    plotaSinal(faseLetraB,wLetraB,"fase Letra B","x-Axis","y-Axis","fase","green",0,0.0035)
    
    plotaSinal(xLetraC,t2,"x(t) Letra C","x-Axis","y-Axis","x(t)","blue",0,1)
    plotaSinal(XLetraC,wLetraC,"X(jw) Letra C","x-Axis","y-Axis","X(jw)","red",0,0.15)
    plotaSinal(faseLetraC,wLetraC,"fase Letra C","x-Axis","y-Axis","fase","green",0,0.05)

    plotaSinal(xLetraD,t3,"x(t) Letra D","x-Axis","y-Axis","x(t)","blue",0,1)
    plotaSinal(XLetraD,wLetraD,"X(jw) Letra D","x-Axis","y-Axis","X(jw)","red",0,0.005)
    plotaSinal(faseLetraD,wLetraD,"fase Letra D","x-Axis","y-Axis","fase","green",0,0.005)
main()

    
