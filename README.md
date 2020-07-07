# Tarea4

Antes de comenzar la explicación de este trabajo realizado en lenguaje de programación Python, se mostrarán las librerias que se importaron.
```
from mpl_toolkits import mplot3d
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
```

## Crear un esquema de modulación BPSK para los bits presentados. Esto implica asignar una forma de onda sinusoidal normalizada (amplitud unitaria) para cada bit y luego una concatenación de todas estas formas de onda.


![alt text](https://github.com/luisgm98/Tarea4/blob/master/Tx.png)

![alt text]()

##  Calcular la potencia promedio de la señal modulada generada.
 

![alt text](https://github.com/luisgm98/Tarea4/blob/master/Rx-2.png)
![alt text](https://github.com/luisgm98/Tarea4/blob/master/RX-1.png)
![alt text](https://github.com/luisgm98/Tarea4/blob/master/RX0.png)
![alt text](https://github.com/luisgm98/Tarea4/blob/master/RX1.png)
![alt text](https://github.com/luisgm98/Tarea4/blob/master/RX2.png)
![alt text](https://github.com/luisgm98/Tarea4/blob/master/RX3.png)


##  Simular un canal ruidoso del tipo AWGN (ruido aditivo blanco gaussiano) con una relación señal a ruido (SNR) desde -2 hasta 3 dB.



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
