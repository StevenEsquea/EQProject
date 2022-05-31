from matplotlib import pyplot as plt
import numpy as np

from pista import Pista
from bus import Bus

def mostrar(rutina, track):
    if (type(track)==Pista.mro()[0]):
        if(track.canales==1):
            fig = plt.figure(figsize=(18,6))
            subfig = fig.add_subplot()

            subfig.plot(rutina(track)[0][1],rutina(track)[0][0], label = track.nombre, linewidth=1)

            pinknoisereference(subfig, track.canales)
            ploter(subfig)

        elif(track.canales==2):
            fig = plt.figure(figsize=(18,12))
            subfig = np.zeros(3, dtype=object)
            subfig[-1]= fig.add_subplot(211)
            subfig[1] = fig.add_subplot(212)
            
            subfig[-1].plot(rutina(track)[-1][1],rutina(track)[-1][0], label = track.nombre, linewidth=1)
            subfig[1].plot(rutina(track)[1][1],rutina(track)[1][0], label = track.nombre, linewidth=1)

            pinknoisereference(subfig, track.canales)
            
            for k in [-1,1]:
                ploter(subfig[k])
            
    if (type(track)==Bus.mro()[0]):
        if(track.canales==1):
            fig = plt.figure(figsize=(18,6))
            subfig = fig.add_subplot()
            
            for i in track.pistas:
                subfig.plot(rutina(i)[-1][1], rutina(i)[-1][0], label = i.nombre, linewidth=1)

            pinknoisereference(subfig, track.canales)
            ploter(subfig)
            
        elif(track.canales==2):
            fig = plt.figure(figsize=(18,12))
            subfig = np.zeros(3, dtype=object)
            subfig[-1]= fig.add_subplot(211)
            subfig[1] = fig.add_subplot(212)
            
            for i in track.pistas:
                subfig[-1].plot(rutina(i)[-1][1], rutina(i)[-1][0], label = i.nombre, linewidth=1)
                subfig[1].plot(rutina(i)[1][1], rutina(i)[1][0], label = i.nombre, linewidth=1)

            pinknoisereference(subfig, track.canales)
            
            for k in [-1,1]:
                ploter(subfig[k])
                
    plt.savefig(track.nombre+".png", dpi=300)
        
def ploter(_subfig):
    _subfig.legend(loc="lower left")
    _subfig.grid(linewidth=1)
    _subfig.grid(which="minor", linewidth=0.5)
    _subfig.set_xscale("log")
    #_subfig.set_yscale("log")
    _subfig.set_xlim(20,22000)
    _subfig.set_ylim(-100,3)
    _subfig.set_xlabel("Frecuencia (Hz)")
    _subfig.set_ylabel("Ganancia (dB)")
    
    xticks10=[i for i in range(20,100,1)]
    xticks100=[i for i in range(100,1000,10)]
    xticks1000=[i for i in range(1000,10000,100)]
    xticks10000=[i for i in range(10000,22000,1000)]
    xticks=xticks10+xticks100+xticks1000+xticks10000

    mainxticksset={20, 30, 40, 50, 60, 70, 80, 90, 100,
                  200,300,400,500,600, 700, 800, 900, 1000,
                  2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000,
                  10000, 13000, 16000, 20000}
    othersx={25,35,150,250,1500,2500}
    mainxtickswithnolabelset={70, 90, 700, 900, 7000, 9000}

    def _majorxticks(xticks, mainset=mainxticksset, mainwithno=mainxtickswithnolabelset, labels=False):
        """"""
        arreglo = []
        if (labels==True):
            for i in xticks:
                if (i in mainset):
                    if (i in mainwithno):
                        arreglo+=[""]
                    elif (i%1000==0):
                        arreglo+=[str(i//1000)+"k"]
                    else:
                        arreglo+=[i]
        else:
            for i in xticks:
                if (i in mainset):
                    arreglo+=[i]
        return arreglo
    """
    def _minorxticks(xticks,othersx=othersx):
        arreglo = []
        for i in xticks:
            if (i in othersx):
                arreglo+=[""]
            else:
                arreglo+=[""]
        return arreglo
    """
    mainxtickslist=_majorxticks(xticks)
    mainxtickslabels=_majorxticks(xticks, labels=True)
    #minorxtickslabels=_minorxticks(xticks)
    minorxtickslabels=["" for i in xticks] # Arreglar la parte comentada tanto con # como con """"""

    _subfig.set_xticks(mainxtickslist, minor=False)
    _subfig.set_xticklabels(mainxtickslabels, minor=False)
    _subfig.set_xticks(xticks, minor=True)
    _subfig.set_xticklabels(minorxtickslabels, minor=True)
    
    mainytickslist = [-100,-90,-80,-70,-60,-50,-40,-30,-20,-10,0]
    minorytickslist= [-i for i in range(1,100)]
    _subfig.set_yticks(mainytickslist, minor=False)
    _subfig.set_yticks(minorytickslist, minor=True)
    
def pinknoisereference(subfig,canales):
    PINK_NOISE = np.load("./lib/PinkNoise/PinkNoiseSpectrum.npy", allow_pickle=True)
    
    if (canales==1):
        subfig.plot(PINK_NOISE[-1][1], PINK_NOISE[-1][0], label = "Pink noise (-18dB)", linewidth=1)
        
    elif (canales==2):
        subfig[-1].plot(PINK_NOISE[-1][1], PINK_NOISE[-1][0], label = "Pink noise (-18dB)", linewidth=1)
        subfig[1].plot(PINK_NOISE[1][1], PINK_NOISE[1][0], label = "Pink noise (-18dB)", linewidth=1)