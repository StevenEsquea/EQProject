import numpy as np

class Bus:
    def __init__(self, *args, nombre="",):
        self.pistas = self._pistas(args)
        self.nombre = "bus" if (nombre=="") else nombre
        self.canales = self._canales()        
        
    def _canales(self):
        for i in self.pistas:
            if (i.canales==2):
                return 2
        return 1
    def _pistas(self, entrada):
        entrada = np.array(entrada)
        
        if (entrada.ndim==2):
            entrada = entrada[0]
            
            return entrada
        
        return entrada