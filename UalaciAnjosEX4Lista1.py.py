# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 20:52:38 2021

@author: Uálaci dos Anjos
"""

import numpy as np
from numpy import pi
import matplotlib.pyplot as plt


def plotaSinal(f,t,titulo):
    fig, ax1 = plt.subplots()
    ax1.plot(t, f, 'c-', linewidth=2)
    ax1.axhline(y=0, color='k')
    ax1.axvline(x=0, color='k')
    ax1.set_xlabel("Tempo")
    ax1.set_ylabel("Amplitude")
    ax1.grid(True)
    ax1.set_title(titulo)
    fig.tight_layout()
    plt.show()
    
def degrau(t,amplitude, deslocamento, tam):
    
    u = np.zeros(tam)
    for i in range (0,tam):
        if t[i] >= -deslocamento:
            u[i] = amplitude
    return u
    
def main():
    t = np.arange(-10, 20, 0.001)
    t3 = np.arange(-10, -6, 0.001)
    t5 = np.arange(-14, 16, 0.001)
    y2 = []
    #t = np.linspace(-10,10,1000)
    #como x1 e x2 do enunciado do exercicio possuem o mesmo valor
    #no intervalo de -10 a 20, nao havera diferenca na analise desse intervalo
    tam = len(t)
    x0 = 0*t3
    x1 = np.cos((pi/6)*t)
    x2 = np.cos((pi/6)*t)
    x1Deslocado = np.cos((pi/6)*t5)
    degrau(t,1,-4, tam)
    
    y1 = x1+0.9*x1Deslocado
    
    for i in range (0,len(x0)):
        y2.append(x0[i])
    
    for i in range(0, len(x2)-4000):
        y2.append(x2[i])
    
    plotaSinal(y2,t, 'x2 Deslocado')
    
    for i in range (0, len(y2)):
        y2[i] = 0.9*y2[i]+x2[i]
    
    plotaSinal(x2,t, 'x2')    
    plotaSinal(y2,t, 'y2 = x2[n]+0.9x2[n-4]')
    
    plotaSinal(x1,t, 'x1')
    plotaSinal(x1Deslocado,t, 'x1Deslocado')    
    plotaSinal(y1,t, 'y1 = x1[n]+0.9x1[n-4]')

    
    y3 = -x1*degrau(t,1,3, tam)
    
    plotaSinal(degrau(t,1,3, tam),t, 'u[n+3]')
    plotaSinal(-x1,t, '-x1[n]')
    plotaSinal(y3,t, 'y3 = x1[-n]*u[n+3]')
    
    y4=[]
    
    for i in range (0,30000):
        if (i <= 20000):
            y4.append(-x2[i])
        
        else:
            y4.append(0)
        
    u = degrau(t,1,3, tam)
    plotaSinal(y4,t, '-x2[n]')
    
    for i in range (0,30000):
        y4[i] = y4[i]*u[i]
            
    plotaSinal(y4,t, 'y4 = x2[-n]*u[n+3]')

    u = degrau(t,1,-5, tam)
    y5 = x1*u
    plotaSinal(u,t, 'u[n-5]')
    plotaSinal(y5,t, 'y5 = x1[n]*u[n-5]')
    
    y6 = x1*(degrau(t,1,-5, tam)-degrau(t,1,-10, tam))
    plotaSinal(degrau(t,1,-5,tam),t, 'u[n-5]')
    plotaSinal(degrau(t,1,-10,tam),t, 'u[n-10]')
    plotaSinal(y6,t, 'y6 = x1[n]*(u[n-5]-u[n-10])')
    
    u = degrau(t,1,1,tam)
    y7 = x1+u
    plotaSinal(u,t, 'u[n-10]')
    plotaSinal(y7,t, 'y7 = x1[n]*u(n+1)')
    
main()