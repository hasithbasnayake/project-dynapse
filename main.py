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

  # Define size of DoG

  DoG["Size"]["Pix"] = PixelSize
  DoG["Size"]["Ang"] = np.ceil(DoG["Size"]["Pix"] / PPA) 

  # Define centre

  DoG["Centre"]["Sigma"]["Pix"] = Sigmas[0]
  DoG["Centre"]["Sigma"]["Ang"] = DoG["Centre"]["Sigma"]["Pix"] / PPA
  DoG["Centre"]["Kernel"] = gen_gaussian_kernel(DoG["Size"]["Pix"], DoG["Centre"]["Sigma"]["Pix"])

  # Define surround

  DoG["Surround"]["Sigma"]["Pix"] = Sigmas[1]
  DoG["Surround"]["Sigma"]["Ang"] = DoG["Surround"]["Sigma"]["Pix"] / PPA
  DoG["Surround"]["Kernel"] = gen_gaussian_kernel(DoG["Size"]["Pix"], DoG["Surround"]["Sigma"]["Pix"])


  # Difference of gaussians, depending on whether ON-Centre OFF-Surround or OFF-Centre ON-Surround

  if OnOff == "on":
    DoG["Kernel"] = DoG["Centre"]["Kernel"] - DoG["Surround"]["Kernel"]
  if OnOff == "off":
    DoG["Kernel"] = -DoG["Centre"]["Kernel"] + DoG["Surround"]["Kernel"]

  # Normalization, sum-to-zero

  DoG["Kernel"] = DoG["Kernel"] - np.mean(DoG["Kernel"])
    
  # Normalization, max output =1 
  
  input_min = 0
  input_max = 1 

  # DoG["Kernel"] /= (np.sum(np.abs(DoG["Kernel"])) / 2) * (input_max - input_min) 

  return DoG 

# Creating the patch size

PatchSize["Pix"] = np.array([28,28])
PatchSize["Ang"] = np.array([8,8])

# Create kernel that will represent the center surround 

tKSizeOFF["Pix"] = np.array([9,9])
tKSizeOFF["Ang"] = np.ceil(tKSizeOFF["Pix"] / PPA)

# Set center parameters 

tSigmaCentreSurroundOFF["Pix"] = np.array([(1/3) * tKSizeOFF["Pix"][0], (2/3) * tKSizeOFF["Pix"][0]] )
tSigmaCentreSurroundOFF["Ang"] = tSigmaCentreSurroundOFF["Pix"] / PPA


print(tKSizeOFF["Ang"])
print(tSigmaCentreSurroundOFF["Pix"])
print(tSigmaCentreSurroundOFF["Ang"])

kernel_off = DoG(tKSizeOFF["Pix"], PPA, tSigmaCentreSurroundOFF["Pix"], 'off')
kernel_on = DoG(tKSizeOFF["Pix"], PPA, tSigmaCentreSurroundOFF["Pix"], 'on')
plt.imshow(kernel_off["Kernel"], cmap="grey")

from scipy.signal import convolve2d
from skimage import data as example_images
camera_man = example_images.camera()

table = plt.figure()
table = plt.figure(figsize=(15,10))

table.add_subplot(1,2,1)
plt.imshow(convolve2d(camera_man, kernel_off["Kernel"], mode='same'), cmap ="gray")
plt.title("Off-Center")
plt.axis("off")

table.add_subplot(1,2,2)
plt.imshow(convolve2d(camera_man, kernel_on["Kernel"], mode='same'), cmap ="gray")
plt.title("On-Center")
plt.axis("off")
