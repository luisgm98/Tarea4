# Tarea4

Antes de comenzar la explicación de este trabajo realizado en lenguaje de programación Python, se mostrarán las librerias que se importaron.
```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from scipy import signal

```

## Crear un esquema de modulación BPSK para los bits presentados. Esto implica asignar una forma de onda sinusoidal normalizada (amplitud unitaria) para cada bit y luego una concatenación de todas estas formas de onda.
La modulación BPSK o modulación binaria por desplazamiento de fase, se encarga de representar los bits de la señal moduladora como una onda sinusoidal cuando el bit corresponde a un uno, mientras que cuando el bit corresponde a un cero, será representado como una onda sinusoidal negativa. Por lo tanto, un "1" de la señal moduladora se representará como se muetra en la siguiente figura:

![alt text](https://github.com/luisgm98/Tarea4/blob/master/seno.png)

Se trabaja a una frecuencia de 5 kHz, por lo que el periodo corresponde a 200 μs, tal y como se observa en la figura anterior.

Para calcular la modulación BPSK de los bits contenidos en el archivo "bits10k.csv", se procedió a crear la siguiente función:
```
def bpsk(bits):
    for k, b in enumerate(bits):
        if b == 1:
            senal[k*p:(k+1)*p]= seno
        else:
            senal[k*p:(k+1)*p]= -seno   
```

Luego, graficando los primeros 5 bits de la señal ya modulada con 50 puntos de muestreo, para una frecuencia de muestreo de 250 kHz, se obtuvo lo siguiente:

![alt text](https://github.com/luisgm98/Tarea4/blob/master/Tx.png)


##  Calcular la potencia promedio de la señal modulada generada.
 
Para este enunciado, fue necesario calcular la potencia instantanea de la señal transmitida, definida como el cuadrado de la señal en cada punto, ya que la señal es discreta. Luego, para la potencia promedio era necesario realizar una integración de la potencia intantanea, lo cual se realizó aplicando una integración trapezoidal con ayuda de la función "integrate". El código utilizado fue el siguiente:
```
#Potencia instantanea
Pins = senal**2

#Potencia promedio
Ps = integrate.trapz(Pins,ts) /(N*T) 
```
Lo anterior nos dio como resultado una potencia promedio de la señal modulada de 0.4900009800019598 W.

##  Simular un canal ruidoso del tipo AWGN (ruido aditivo blanco gaussiano) con una relación señal a ruido (SNR) desde -2 hasta 3 dB.

Es importante recordar el la ecuación de la relación señal a ruido, o SNR:
![alt text](https://github.com/luisgm98/Tarea4/blob/master/ruido.PNG)

Para este enunciado, se procede a despejar de la ecuación anterior el Pn, correspondiente a la potencia del ruido. Luego, para crear el ruido se utilizó la función "random" de la libreria de "numpy" y se procedió a calcularlo con una distribución normal y una desviación estandar igual a la raiz cuadrada de Pn. Este ruido se le suma a la señal transmitida ya que es aditivo. Importante recalcar que se calculó para SNR de -2, -1, 0, 1, 2 y 3  dB. 
Las siguientes imagenes nos muestran la señal recibida para cada valor de SNR calculado, solo se muestran los primeros 5 bits.

![alt text](https://github.com/luisgm98/Tarea4/blob/master/Rx-2.png)
![alt text](https://github.com/luisgm98/Tarea4/blob/master/RX-1.png)
![alt text](https://github.com/luisgm98/Tarea4/blob/master/RX0.png)
![alt text](https://github.com/luisgm98/Tarea4/blob/master/RX1.png)
![alt text](https://github.com/luisgm98/Tarea4/blob/master/RX2.png)
![alt text](https://github.com/luisgm98/Tarea4/blob/master/RX3.png)

##  Graficar la densidad espectral de potencia de la señal con el método de Welch (SciPy), antes y después del canal ruidoso.

![alt text](https://github.com/luisgm98/Tarea4/blob/master/ACR-2.png)
![alt text](https://github.com/luisgm98/Tarea4/blob/master/DCR-2.png)
![alt text](https://github.com/luisgm98/Tarea4/blob/master/ACR-1.png)
![alt text](https://github.com/luisgm98/Tarea4/blob/master/DCR-1.png)
![alt text](https://github.com/luisgm98/Tarea4/blob/master/ACR0.png)
![alt text](https://github.com/luisgm98/Tarea4/blob/master/DCR0.png)
![alt text](https://github.com/luisgm98/Tarea4/blob/master/ACR1.png)
![alt text](https://github.com/luisgm98/Tarea4/blob/master/DCR1.png)
![alt text](https://github.com/luisgm98/Tarea4/blob/master/ACR2.png)
![alt text](https://github.com/luisgm98/Tarea4/blob/master/DCR2.png)
![alt text](https://github.com/luisgm98/Tarea4/blob/master/ACR3.png)
![alt text](https://github.com/luisgm98/Tarea4/blob/master/DCR3.png)



## Demodular y decodificar la señal y hacer un conteo de la tasa de error de bits (BER, bit error rate) para cada nivel SNR.


## Graficar BER versus SNR.

![alt text](https://github.com/luisgm98/Tarea4/blob/master/BERvsSNR.png)
