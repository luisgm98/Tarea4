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

En este enunciado, se utilizó la biblioteca "scipy", la cual nos provee una función que se encarga de calcular la densidad espectral de potencia de la señal mediante el método de Welch. Esta función recibe como argumento la frecuencia de muestreo y la onda transmitida, es decir, Tx, para antes del canal ruidoso; mientras que para después del canal ruidoso, se utiliza onda recibida, es decir, Rx. El código utilizado fue el siguiente:

```
#Antes del canal ruidoso
fw, PSD = signal.welch(senal, fm, nperseg=1024)
    
#Después del canal ruidoso
fw, PSD = signal.welch(Rx, fm, nperseg=1024)
```
Además, se procedió a graficar cada una para cada valor de SNR, obteniendo como resultado las siguientes gráficas. Además, se puede observar que la densidad es practicamente la misma para todos los valores de SNR.

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

Para realizar la desmodulación y la decodificación, se comienza por calcular la pseudo energía de la onda original, la cual corresponde a la sumatoria del cuadrado de cada valor de la onda del seno, ya que es discreto. Esta pseudo energía nos servirá para definir el umbral y saber si la señal recibida corresponde a un cero o a un uno. El umbral que se definió fue un medio de la pseudo energía, es decir, si el producto interno de dos funciones es mayor a este umbral, el bit corresponde a un uno, mientras que en caso contrario, corresponderia a un  cero. Importante señalar que se realiza una desmodulación coherente, es decir, se conoce el inicio y el final del periodo, cosa que no ocurre en todos los casos. 
Luego se procedió a calcular la tasa de error de bits para cada nivel de SNR, para esto se realizó una suma del valor absoluto de la diferencia entre los bits transmitidos y los recibidos, lo cual nos da como resultado la cantidad de errores que se presentaron. Luego, para calcular el BER se procedió a dividir la cantidad de errores entre el número total de bits, el cual es de 10000 bits. El código utilizado fue el siguiente:
```
#Calculamos la pseudo energía de la onda original 
Es = np.sum(seno**2)

#Inicialización de los bits decodificados
bitsRx = np.zeros(N)

#Demodulación coherente: sabemos el inicio y el final de un periodo
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

print("Para un SNR de", i, "tenemos", error,"errores, con un BER de", BER)
```

Los resultados que se obtuvieron son los siguientes:
```
Para un SNR de -2 tenemos 14.0 errores, con un BER de 0.0014
Para un SNR de -1 tenemos 6.0 errores, con un BER de 0.0006
Para un SNR de 0 tenemos 1.0 errores, con un BER de 0.0001
Para un SNR de 1 tenemos 0.0 errores, con un BER de 0.0
Para un SNR de 2 tenemos 0.0 errores, con un BER de 0.0
Para un SNR de 3 tenemos 0.0 errores, con un BER de 0.0
```

Podemos observar que la mayor cantidad de errores se da para un SNR de -2, lo cual era de esperarse, ya que entre mayor sea el SNR, menos errores debido a que el ruido es menor
A modo de experimento personal, se definió un umbral de 0, para lo cual se obtuvieron cero errores para todos los valores SNR. 

## Graficar BER versus SNR.

Esta gráfica nos sirve para observar mejor los resultados obtenidos en el enunciado anterior. Podemos observar como disminuye la cantidad de errores al aumentar SNR.

![alt text](https://github.com/luisgm98/Tarea4/blob/master/ber.png)
