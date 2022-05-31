from itertools import count
import numpy as np
"""
def promedio(f_x, _x, n=10):
    _CHUNK_SIZE = 2**n
    
    if (f_x.size%_CHUNK_SIZE!=0):
        f_x = muestral_completer(f_x, _CHUNK_SIZE)

    f_x_prom = np.zeros(0)
    _x_prom = np.zeros(0)
    for i in range(f_x.size//_CHUNK_SIZE-1):
        _DX = _x[(i+1)*_CHUNK_SIZE] - _x[i*_CHUNK_SIZE]
        f_x_trozo = np.abs(f_x[i*_CHUNK_SIZE:(i+1)*_CHUNK_SIZE])
        _x_trozo = _x[i*_CHUNK_SIZE:(i+1)*_CHUNK_SIZE]
        
        nuevo_valor_f_x_prom = (1/_DX)*(integral_muestral(f_x_trozo, _x_trozo))
        nuevo_valor_x = _x[i*_CHUNK_SIZE] + _DX/2
        
        f_x_prom = np.append(f_x_prom, nuevo_valor_f_x_prom)
        _x_prom = np.append(_x_prom, nuevo_valor_x)
        
    return np.array([f_x_prom, _x_prom])
"""

def promedio(f_x, _x, n=10, algoritmo="abs"):
    _CHUNK_SIZE = 2**n
    
    if (f_x.size%_CHUNK_SIZE!=0):
        f_x = muestral_completer(f_x, _CHUNK_SIZE)

    f_x_prom = np.zeros(0)
    _x_prom = np.zeros(0)
    
    if (algoritmo=="rms"):
        for i in range(f_x.size//_CHUNK_SIZE-1):
            _DX = _x[(i+1)*_CHUNK_SIZE] - _x[i*_CHUNK_SIZE]
            f_x_trozo = np.abs((f_x[i*_CHUNK_SIZE:(i+1)*_CHUNK_SIZE]))**2
            _x_trozo = _x[i*_CHUNK_SIZE:(i+1)*_CHUNK_SIZE]

            nuevo_valor_f_x_prom = np.sqrt((1/_DX)*(integral_muestral(f_x_trozo, _x_trozo)))
            nuevo_valor_x = _x[i*_CHUNK_SIZE] + _DX/2

            f_x_prom = np.append(f_x_prom, nuevo_valor_f_x_prom)
            _x_prom = np.append(_x_prom, nuevo_valor_x)

        return np.array([f_x_prom, _x_prom])
    elif (algoritmo=="abs"):
        for i in range(f_x.size//_CHUNK_SIZE-1):
            _DX = _x[(i+1)*_CHUNK_SIZE] - _x[i*_CHUNK_SIZE]
            f_x_trozo = np.abs(f_x[i*_CHUNK_SIZE:(i+1)*_CHUNK_SIZE])
            _x_trozo = _x[i*_CHUNK_SIZE:(i+1)*_CHUNK_SIZE]

            nuevo_valor_f_x_prom = (1/_DX)*(integral_muestral(f_x_trozo, _x_trozo))
            nuevo_valor_x = _x[i*_CHUNK_SIZE] + _DX/2

            f_x_prom = np.append(f_x_prom, nuevo_valor_f_x_prom)
            _x_prom = np.append(_x_prom, nuevo_valor_x)

        return np.array([f_x_prom, _x_prom])
    else:
        return "¡Algoritmo no disponible!"

def integral_muestral(f_m, _m, algoritmo="med"):
    if (algoritmo=="der"):
        suma = 0
        
        for i in range(f_m.size-1):
            suma = suma + f_m[i]*(_m[i+1]-_m[i])

        return suma

    elif (algoritmo=="med"):
        suma = 0
        
        for i in range(f_m.size-1):
            suma = suma + (f_m[i]+(f_m[i+1]-f_m[i])/2)*(_m[i+1]-_m[i])

        return suma

    elif (algoritmo=="izq"):
        suma = 0

        for i in range(f_m.size-1):
            suma = suma + (f_m[i]+(f_m[i+1]-f_m[i])/2)*(_m[i+1]-_m[i])

        return suma

    else:
        print("¡Error!")
        print('El algoritmo elegido no es válido. Debe ser uno "izq", "der" o "med".')
        
def muestral_completer(data, chunksize):
    _data_initial_size = data.size
    for i in count():
        if (_data_initial_size+i)%chunksize==0:
            _adicionales = i
            break
            
    return np.append(data, np.zeros(_adicionales, dtype=data.dtype))