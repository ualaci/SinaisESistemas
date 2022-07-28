# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 14:57:52 2021

@author: Uálaci dos Anjos
"""

import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

#Suponha que um sistema H do tipo LTI com resposta impulso h[n] é aplicado um sinal x[n].
def plotaSinal(f,t,titulo):
    fig, ax1 = plt.subplots()
    ax1.stem(t, f, linefmt='r-',use_line_collection=True)
    #ax1.plot(t, f, 'c-', linewidth=2)
    ax1.axhline(y=0, color='k')
    ax1.axvline(x=0, color='k')
    ax1.set_xlabel("amostra")
    ax1.set_ylabel("Amplitude")
    ax1.grid(True)
    ax1.set_title(titulo)
    fig.tight_layout()
    plt.show()
    
def main():
    upperLimit = 20
    lowerLimit=-2
    n = np.arange(lowerLimit, upperLimit,1)
    i=0
    j=0
    x=np.ones(abs(lowerLimit)+abs(upperLimit))
    x[n<0]=0
    
    h1=(1/2)**n
    h1[np.logical_and(n >= -2, n < 0)]=0
    
    h2=np.zeros(abs(lowerLimit)+abs(upperLimit))
    h2[n==0]=1
    h2[n==1]=-1
    
    h3=float(-1)**n
    h3[n>=4]=0
    
    h4=np.ones((abs(lowerLimit)+abs(upperLimit)))
    h4[n<0]=0
    
    h5=-n
    h5[np.logical_and(n >= -2, n < 0)]=0
    
    h6=np.sin((1/12)*pi*n)
    h6[np.logical_and(n >= -2, n < 2)]=0

    y1 = np.convolve(h1,x)
    y2 = np.convolve(h2,x)
    y3 = np.convolve(h3,x)
    y4 = np.convolve(h4,x)
    y5 = np.convolve(h5,x)
    y6 = np.convolve(h6,x)
    
    Y1=[]
    Y2=[]
    Y3=[]
    Y4=[]
    Y5=[]
    Y6=[]
    
    for i in range(abs(lowerLimit)-1,int((len(y1)/2)+abs(lowerLimit))):
        Y1.append(y1[i])
    
    for i in range(abs(lowerLimit)-1,int((len(y2)/2)+abs(lowerLimit))):
        Y2.append(y2[i])
    
    for i in range(abs(lowerLimit)-1,int((len(y3)/2)+abs(lowerLimit))):
        Y3.append(y3[i])
    
    for i in range(abs(lowerLimit)-1,int((len(y4)/2)+abs(lowerLimit))):
        Y4.append(y4[i])
    
    for i in range(abs(lowerLimit)-1,int((len(y5)/2)+abs(lowerLimit))):
        Y5.append(y5[i])
    
    for i in range(abs(lowerLimit)-1,int((len(y6)/2)+abs(lowerLimit))):
        Y6.append(y6[i])
    
    m=np.arange(-2,len(y1)-2,1)
    
    #SAIDA Y COM INTERVALO [-2,20]
    plotaSinal(Y1,n, "y[n]=u[n]*(1/2)^n u[n]")
    plotaSinal(Y2, n, "y[n]=u[n]*impulso[n]-impulso[n-1]")
    plotaSinal(Y3, n, "y[n]=u[n]*(-1)^n[u[n+2]-u[n-3]")
    plotaSinal(Y4, n, "y[n]=u[n]*u[n]")
    plotaSinal(Y5, n, "y[n]=u[n]*-n u[n]")
    plotaSinal(Y6, n, "y[n]=u[n]*sen[(1/12)pi*n]*u[n-3]")
    
    """
    #SAIDA Y COM INTERVALO COMPLETO CASO QUEIRA VISUALIZAR
    plotaSinal(y1,m, "y[n]=u[n]*(1/2)^n u[n]")
    plotaSinal(y2, m, "y[n]=u[n]*impulso[n]-impulso[n-1]")
    plotaSinal(y3, m, "y[n]=u[n]*(-1)^n[u[n+2]-u[n-3]")
    plotaSinal(y4, m, "y[n]=u[n]*u[n]")
    plotaSinal(y5, m, "y[n]=u[n]*-n u[n]")
    plotaSinal(y6, m, "y[n]=u[n]*sen[(1/12)pi*n]*u[n-3]")
    """
    
main()