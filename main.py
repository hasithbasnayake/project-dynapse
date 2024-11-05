# Import statements

import numpy as np
import matplotlib.pyplot as plt

# Declaration of PPA, patch-size, and num filters

PPA = np.array([8,8]) # Pixels Per Arc (PPA) represents angular dimensions, denoting how many pixels represent a degree of visual angle change

PatchSize = {
    "Pix" : None,
    "Ang" : None
}

tKSizeOFF = {
    "Pix" : None,
    "Ang": None
}

tSigmaCentreSurroundOFF = {
    "Pix": None,
    "Ang": None
}

def gen_gaussian_kernel(shape=(3,3),sigma=0.5):
    """
    2D gaussian mask - should give the same result as MATLAB's
    fspecial('gaussian',[shape],[sigma])
    """
    m,n = [(ss-1.)/2. for ss in shape]
    y,x = np.ogrid[-m:m+1,-n:n+1]
    h = np.exp( -(x*x + y*y) / (2.*sigma*sigma) )
    h[ h < np.finfo(h.dtype).eps*h.max() ] = 0
    sumh = h.sum()
    if sumh != 0:
        h /= sumh
    return h

def DoG(PixelSize, PPA, Sigmas, OnOff):
  #PixelSize must be odd 
  DoG = {
      "Size": {
          "Pix": None,
          "Ang": None
      },
      "Centre": {
          "Sigma" : {
              "Pix": None,
              "Ang": None
          },
          "Kernel" : None
      },
      "Surround": {
          "Sigma" : {
              "Pix": None,
              "Ang": None
          },
          "Ang" : None,
          "Kernel" : None
      },
      "Kernel" : None
  }