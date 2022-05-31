from itertools import count
import numpy as np
from scipy import fft

from pista import Pista
from bus import Bus
from mates import muestral_completer, promedio
import dbs

def espectro_mono(track, _TASA_DE_MUESTREO, n=10):
    _track = track
    _CHUNK_SIZE=2**n

    if (_track.size%_CHUNK_SIZE!=0):
        _track = muestral_completer(_track, _CHUNK_SIZE)

    _espectro = fft.rfft(_track)
    _frecuencias = fft.rfftfreq(_track.size, 1/_TASA_DE_MUESTREO)
    
    _promedio = promedio(_espectro, _frecuencias) #Aquí se suaviza el espectro.
    _promedio[0] = _promedio[0]/np.iinfo(np.int16).max #Aquí se normaliza.
    _promedio[0] = dbs.abstodB(_promedio[0])

    return _promedio

def espectro(track):
    if (type(track)==Pista.mro()[0]):
        try:
            return track.espectro
        except (NameError, AttributeError):
            if (track.canales==1):
                _espectro = espectro_mono(track.onda[0], track.TASA_DE_MUESTREO)
                track.espectro = np.array([_espectro,_espectro,_espectro])

            elif (track.canales==2):
                track.espectro = np.zeros(3, dtype=np.ndarray)
                j = [-1,1]
                for i in j:
                    track.espectro[i] = espectro_mono(track.onda[i], track.TASA_DE_MUESTREO)
            else:
                print("Esquema de sonido no reconocido")
                
            return track.espectro
            
    elif (type(track)==Bus.mro()[0]):
        for pista in track.pistas:
            espectro(pista)