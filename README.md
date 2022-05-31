# **EQProject**
Siendo parte de un proyecto mayor, de momento es una herramienta que calcula y visualiza el espectro sonoro a partir de archivos de audio.

## **Creadores:**
Programa creado por **Steven Esquea** con la valiosa ayuda de **Angi Pardo**.

## **Versión:**
0.2

## **Dependencias:**

El programa requiere del intérprete de Python 3. Su desarrollo se ha hecho con
base en:

> Python 3.8.3rc1

Por lo que se recomienda encarecidamente tener esa versión instalada o una. No
obstante, se espera que el programa funcione bien para Python 3.6 o versiones
superiores.

EQProject necesita las siguientes librerías de Python

* Numpy
* Scipy
* Matplotlib

En particular, el funcionamiento del programa se ha probado con las siguientes
versiones de las librerías anteriores:

* Numpy 1.18.4
* Scipy 1.4.1
* Matplotlib 3.2.1


## **Cambios en las versiones:**

Versión	|	Cambio, respecto a la versión inmediatamente anterior
-------	|	-----------------------------------------------------
0.1.1	|	El espectro se guarda y se muestra ahora en dB.
0.1.2	|	El espectro del ruido rosado, que actúa como referencia, ahora está almacenado de forma permanente, así, que no se calcula cada vez que se ejecuta la app, mejorando así la velocidad de ejecución.
0.2		|	Se cambió la estructura de archivos, para hacer darle más orden al programa. Nota: python usa como punto base de las rutas relativas no el lugar donde está almacenado el script, sino el lugar desde donde se ejecuta.
