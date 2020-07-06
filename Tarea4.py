# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 17:49:04 2020

@author: luisg
"""


 # -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 21:12:05 2020

@author: luisg
"""


# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 19:29:42 2020

@author: luisg
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from scipy import signal

"--------------------------------------------------------------------------"
#Leemos los datos del archivo 'bits10k' y los almacenamos en bits
datos = pd.read_csv('bits10k.csv',header=None)


bits= []

for i in range(0,len(datos)):
    bits.append(datos.iloc[i][0])

#Definimos la frecuencia a la que vamos a trabajar:
f = 5000  #f= 5 kHz

#Definimos el periodo de simbolo
T = 1/f   # T = 200 us

#Número de bits
N = len(bits)  # N = 10k
print(N)

#Número de puntos por muestreo
p = 50

#Frecuencia de muestreo 
fm = f*p

#Creamos el vector de tiempo de muestreo
t = np.linspace(0,T,p)

#Creación de un vector tiempo para toda la señal
ts = np.linspace(0,T*N,p*N)


#Creamos la función seno
seno = np.sin(2*np.pi*f*t)

"----------------------------------------------------------------------------------------"
"Enunciado1"
"Crear un esquema de modulación BPSK para los bits presentados." 
"Esto implica asignar una forma de onda sinusoidal normalizada (amplitud unitaria)"
"para cada bit y luego una concatenación de todas estas formas de onda"

#Creamos el vector de la señal
senal = np.zeros(len(ts))

#Creamos una función que se encargue de realizar la modulación BPSK
def bpsk(bits):
    for k, b in enumerate(bits):
        if b == 1:
            senal[k*p:(k+1)*p]= seno
        else:
            senal[k*p:(k+1)*p]= -seno
    
bpsk(bits)

#Cantidad de bits que quiero representar
pb = 5


#Graficamos la onda transmitida Tx
plt.figure()
plt.plot(senal[0:pb*p])
plt.title("Tx")
plt.ylabel("Mangnitud de onda")
plt.xlabel("Tiempo [s]")
plt.show()

"-------------------------------------------------------------------------"
"Enunciado 2."
"Calcular la potencia promedio de la señal modulada generada."

#Calculamos la potencia instantanea
Pins = senal**2

#Potencia promedio
Ps = integrate.trapz(Pins,ts) /(N*T) 

print("La potencia promedio es de:",Ps,"W")

"-------------------------------------------------------------------------"
"Enunciado 3."
"Simular un canal ruidoso del tipo AWGN (ruido aditivo blanco gaussiano)"
"con una relación señal a ruido (SNR) desde -2 hasta 3 dB."

BERlist = []
SNRlist = []

for i in range(-2,4):
    #Relación señal-a-ruido deseada
    SNR = i #de -2 a 3  
    SNRlist.append(i)
    
    #Potencia del ruido para SNR y potencia de la señal dada
    #Despejando de SNR (dB) = 10*log(Ps/Pn)
    Pn = Ps /(10**(SNR/10))
    
    #Desviación estandar del ruido
    sigma = np.sqrt(Pn)
    
    #Creamos el ruido con media cero,desviación estrandar(Pn = sigma^2)
    #Se le suma a la señal, ya que es aditivo
    noise = np.random.normal(0,sigma,senal.shape)
    
    # Simular "el canal":señal recibida
    Rx = senal + noise 

    #Visualización de los bits recibidos, con ruido
    plt.figure()
    plt.plot(Rx[0:pb*p])
    plt.title("Rx con SNR de "+str(i))
    plt.ylabel("Mangnitud de onda")
    plt.xlabel("Tiempo [s]")
    plt.show()
    
    

    "-----------------------------------------"
    "Enunciado 4."
    "Graficar la densidad espectral de potencia de la señal con el método de Welch (SciPy), antes y después del canal ruidoso."
    #Antes del canal ruidoso
    fw, PSD = signal.welch(senal, fm, nperseg=1024)
    plt.figure()
    plt.semilogy(fw, PSD)
    plt.title("Antes del canal ruidoso, SNR = "+str(i))
    plt.xlabel("Frecuencia [Hz]")
    plt.ylabel("Densidad espectral de potencia  [V^2/Hz]")
    plt.show()
    
    # Después del canal ruidoso
    fw, PSD = signal.welch(Rx, fm, nperseg=1024)
    plt.figure()
    plt.semilogy(fw, PSD)
    plt.title("Despues del canal ruidoso, SNR = "+str(i))
    plt.xlabel("Frecuencia [Hz]")
    plt.ylabel("Densidad espectral de potencia [V^2/Hz]")
    plt.show()

    "---------------------------------------"
    "Enunciado 5."
    "Demodular y decodificar la señal y hacer un conteo de la tasa de error de bits (BER, bit error rate) para cada nivel SNR."

    #Calculamos la energía de la onda original 
    Es = np.sum(seno**2)

    #Inicialización de los bits decodificados
    bitsRx = np.zeros(N)

    #Creamos una función que se encargue de realizar la demodulación
    #Modulación coherente: sabemos el inicio y el final de un periodo

    for k, b in enumerate(bits):
        #Producto interno de dos funciones
        Ep = np.sum(Rx[k*p:(k+1)*p]*seno)
        if Ep > Es/2:
            bitsRx[k] = 1
        else:
            bitsRx[k] = 0

    #Conteo de errores
    error = np.sum(abs(bits-bitsRx))

    #Bit error rate (BER)
    BER = (error/N)
    BERlist.append(BER)
    
    print("Para un SNR de", i, "tenemos", error,"errores, con un BER de", BER)

"---------------------------------"
"Enunciado 6."
"Graficar BER versus SNR."
plt.figure()
plt.bar(SNRlist,BERlist)
plt.title("BER vs SNR")
plt.ylabel("BER")
plt.xlabel("SNR")
plt.show()