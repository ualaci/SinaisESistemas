# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 18:48:24 2021

@author: Uálaci dos Anjos
"""


import numpy as np
from numpy import pi
from scipy import signal as sinal
import matplotlib.pyplot as plt


def main():

    t = np.arange(0,48,1)
    wt = pi/8*t
    x = sinal.square(wt,0.5)
    
    
    # PLOTANDO O GRÁFICO DA FUNÇÃO x(t)
    fig1, ax1 = plt.subplots()
    ax1.stem(t, x, linefmt='b-',use_line_collection=True)
    
    ax1.axhline(y=0, color='red')
    plt.xlabel("Amplitude")
    plt.ylabel("Amostragem")
    plt.grid()
    ax1.legend()
    ax1.set_title('x[n] = square[n*pi/8]')
    
    plt.show()

main()




