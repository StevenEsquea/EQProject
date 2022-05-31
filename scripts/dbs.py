import numpy as np

def resolution(n):
    x = 10*n*np.log10(4)+10*np.log10(3/2)
    return x

def abstodB(x):
    """Transforma de valores absolutos de muestreo a dB"""
    x_max = np.iinfo(np.int16).max
    x_min = 1
    dB_x_min = -1*resolution(16)
    A = dB_x_min/np.log10(x_min/x_max)
    
    return A*np.log10(x/x_max)

def dBtoabs(x_dB):
    x_max = np.iinfo(np.int16).max
    x_min = 1
    dB_x_min = -1*resolution(16)
    A = dB_x_min/np.log10(x_min/x_max)
    
    return x_max*(10**(x_dB/A))