# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 17:22:13 2021

@author: Uálaci dos Anjos
"""

import numpy as np
from numpy import pi
import matplotlib.pyplot as plt


def plotaSinal(yD,yC,n,t):
    #criando os gráficos
    fig, ax = plt.subplots(2,1)
    ax[0].axhline(y=0, color='k')
    ax[0].axvline(x=0, color='k')
    ax[0].stem(n, yD, linefmt='b-',use_line_collection=True)
    ax[0].set_xlabel("Amostras")
    ax[0].set_ylabel("Amplitude")
    ax[0].grid(True)
    ax[0].set_title('x[n] = 2*cos[n*pi/4]')
    ax[1].plot(t, yC, 'c-', linewidth=2)
    ax[1].axhline(y=0, color='k')
    ax[1].axvline(x=0, color='k')
    ax[1].set_xlabel("Tempo")
    ax[1].set_ylabel("Amplitude")
    ax[1].grid(True)
    ax[1].set_title('x[n] 2*cos[n*pi/4]')
    fig.tight_layout()
    plt.show()
    
def main():
    n = np.arange(-10,10)
    t = np.arange(-10, 10, 0.001)
    sinalDiscreto = 2*np.cos((pi/4)*n)
    sinalContinuo = 2*np.cos((pi/4)*t)
    plotaSinal(sinalDiscreto, sinalContinuo, n, t)
    
main()