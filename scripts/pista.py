import scipy.io.wavfile
import scipy.io as sio
import numpy as np
import re

class Pista:
    def __init__(self, ruta="", nombre=""):
        self.ruta = ruta
        self.nombre = self._nombre(nombre, ruta)
        self._muestreo = sio.wavfile.read(ruta)
        self.TASA_DE_MUESTREO = self._muestreo[0]
        self.canales = self._canales()
        self.onda = self._onda()

    def _canales(self):
        if (self._muestreo[1].ndim==1):
            return 1
        elif (self._muestreo[1].ndim==2):
            return 2

    def _onda(self):
        if (self.canales==1):
            canal_izq = self._muestreo[1]
            canal_der = self._muestreo[1]
            canal_mono = self._muestreo[1]
            
            return np.array([canal_mono, canal_der, canal_izq])
        
        elif (self.canales==2):
            canal_izq = self._muestreo[1].T[0]
            canal_der = self._muestreo[1].T[1]
            canal_mono = canal_izq + canal_der
            
            return np.array([canal_mono, canal_der, canal_izq])
        
    def _nombre(self, nombre, ruta):
        if (nombre==""):
            pattern = r".*\/(.*(\.[wW][aA][vV])?)$"
            return re.match(pattern, ruta).group(1)
        else:
            return nombre
            
        