# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 19:36:37 2021

@author: Uálaci dos Anjos
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 20:39:30 2021

@author: Uálaci dos Anjos
"""

import numpy as np
from numpy import pi
from numpy import abs,cos, sin
from numpy.fft import *
import scipy as sp
import matplotlib.pyplot as plt
from scipy import signal
import random


def plotaSinal(f,t,titulo,xLabel,yLabel,signalType,scale):
    fig, ax1 = plt.subplots()
    if (signalType == 1):        
        ax1.stem(t, f, linefmt='r-',use_line_collection=True)
    
    else: 
        ax1.plot(t, f, 'c-', linewidth=2)

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


def main():
#T = Periodo
#f = Frequencia
#w0 = frequencia angular
#size = tamanho da amostragem

    T = 1
    f = 1/T
    Wo = 2*pi*f
    size = 0.030
    scale=1
    accuracy = 0.0001
    
    C = 2.27364 * 10**(-6)
    R = 100
    wc = 1/(R*C)
    #wc = 700*2*pi
    
    f1=1000
    T1=1/f1
    
    f2=100
    
    w1 =2*pi*f1
    w2=2*pi*f2
    
    jw1 = w1*complex(0,1)
    jw2 = w2*complex(0,1)
    
    
    t = np.arange(0, size, accuracy);
    s = 2.5*sp.signal.square(w1*t)
    ns = 5+2.5*sin(w2*t)
    
    for i in range (0,len(t)):
        ns[i]=random.randint(0,5)+2.5*sin(2*pi*(random.randint(0,100))*t[i])
    
    plotaSinal(ns,t,"ns(t)","tempo","amplitude",0,0.1)
    
    x = s+ns
    xFourier = fft(x)/len(x)
    xFourierShifted = fftshift(xFourier)
    moduleXFourier = np.abs(xFourierShifted)
    
    
    
    k = fftfreq(len(t), f1*size)
    k = fftshift(k)
    
    sFourier = fft(s)/len(s)
    sFourier = fftshift(sFourier)
    
    nsFourier = fft(ns)/len(ns)
    nsFourier = fftshift(nsFourier)
    
    
    plotaSinal(s,t,"s(t)","tempo","amplitude",0,scale)
    #plotaSinal(abs(sFourier),k,"|s(k)|","frequencia","amplitude",1,1)
    plotaSinal(s+ns,t,"x(t)","tempo","amplitude",0,scale)
    plotaSinal(moduleXFourier,k,"|x[k]|","frequencia","Amplitude",1,1)
    

    H1 = jw1/(jw1+wc)
    H1k = H1*k
    h1 = ifft(H1k)*len(t)
    h1 = np.real(h1)
    
    Y1 = H1*sFourier
    Y1 = fftshift(Y1)
    y1 = ifft(Y1)*len(t)
    y1 = np.real(y1)
    
    H2 = jw2/(jw2+wc)
    Y2 = H2*nsFourier
    Y2 = fftshift(Y2)
    y2 = ifft(Y2)*len(t)
    y2 = np.real(y2)
    
    y = y1+y2
    Y = Y1+Y2
    
    #plotaSinal(y1,t,"s(t) recuperado","tempo","amplitude",0,scale)
    #plotaSinal(abs(Y1),k,"|Vc(k) -- RC=0.01|","frequencia","amplitude",1,1)
    
    #plotaSinal(y2,t,"ns(t) filtrado","tempo","amplitude",0,1)
    #plotaSinal(abs(Y2),k,"|ns(k)| filtrado","frequencia","amplitude",1,1)
    
    plotaSinal(h1,t,"H(t)","tempo","amplitude",0,scale)
    plotaSinal(abs(H1k),k,"|H(k)|","frequencia","amplitude",1,1)
    
    plotaSinal(y,t,"x(t) filtrado (y(t)) apos filtragem","tempo","amplitude",0,scale)
    plotaSinal(abs(Y),k,"|x(k) filtrado| (|y(k)|","frequencia","amplitude",1,1)
    
main()
