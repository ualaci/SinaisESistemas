# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 20:39:30 2021

@author: Uálaci dos Anjos
"""

import numpy as np
from numpy import pi
from numpy import abs
from numpy.fft import *
import scipy as sp
import matplotlib.pyplot as plt
from scipy import signal


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
#T = Periodo
#f = Frequencia
#w0 = frequencia angular
#size = tamanho da amostragem
#countT quantidade de periodos da amostragem

    T = 1
    f = 1/T
    w0 = 2*pi*f
    size = 1/(100*f)
    countT = 4
    
    RC1 = 1/100           
    RC2 = 1/10
    RC3 = 1
    
    jw1 = complex(0,1)/RC1 
    jw2 = complex(0,1)/RC2 
    jw3 = complex(0,1)/RC3 
    
    t = np.arange(0, countT*T, size);
    Vs = (sp.signal.square(w0*t, 1/4) * 0.5) + 0.5
    k = fftfreq(len(t), f*size)
    k = fftshift(k)
    
    VsFourier = fft(Vs)/len(Vs)
    VsFourier = fftshift(VsFourier)

    plotaSinal(Vs,t,"Vs(t)","tempo","amplitude",0)
    plotaSinal(abs(VsFourier),k,"|Vs(k)|","frequencia","amplitude",1)
    
    
    H1 = jw1/(jw1+w0)
    Y1 = H1*VsFourier
    Y1 = fftshift(Y1)
    y1 = ifft(Y1)*len(t)
    y1 = np.real(y1)
    
    H2 = jw2/(jw2+w0)
    Y2 = H2*VsFourier
    Y2 = fftshift(Y2)
    
    y2 = ifft(Y2)*len(t)
    y2 = np.real(y2)
    
    H3 = jw3/(jw3+w0)
    Y3 = H3*VsFourier
    Y3 = fftshift(Y3)
    
    y3 = ifft(Y3)*len(t)
    y3 = np.real(y3)
    
    
    plotaSinal(y1,t,"Vc(t) -- RC=0.01","tempo","amplitude",0)
    plotaSinal(abs(Y1),k,"|Vc(k) -- RC=0.01|","frequencia","amplitude",1)
    
    plotaSinal(y2,t,"Vc(t) -- RC=0.1","tempo","amplitude",0)
    plotaSinal(abs(Y2),k,"|Vc(k) -- RC=0.1|","frequencia","amplitude",1)
    
    plotaSinal(y3,t,"Vc(t) -- RC=1","tempo","amplitude",0)
    plotaSinal(abs(Y3),k,"|Vc(k) -- RC=1|","frequencia","amplitude",1)
    
main()
