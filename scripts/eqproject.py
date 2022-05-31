VERSION = "0.1.2"

def main():
    import os
    import re
    import numpy as np
    from pista import Pista
    from bus import Bus
    from visor import mostrar
    from espectro import espectro

    WAVESFILESPATH = ["./waves/","./resources/testingwaves/"]

    try:
        if (len(os.listdir(WAVESFILESPATH[0]))!=0):
            k = 0
        else:
            k = 1
            
        archivos=os.listdir(WAVESFILESPATH[k])
        pistas = np.zeros(0, dtype=Pista.mro()[0])
        for i in archivos:
            pistas = np.append(pistas, Pista(WAVESFILESPATH[k]+i,i))
        bus = Bus(pistas)
        mostrar(espectro, bus)

        print("¡Listo!")

    except FileNotFoundError:
        os.mkdir(WAVESFILESPATH[0])
        
if __name__=="__main__":
    main()
