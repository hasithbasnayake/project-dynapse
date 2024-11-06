# Functions

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
  DoG = DifferenceOfGaussians()

  # Define size of DoG
  
  DoG.Size.Pix = PixelSize
  DoG.Size.Ang = np.ceil(DoG.Size.Pix / PPA)

  # Define centre

  DoG.Centre.Sigma.Pix = Sigmas[0]
  DoG.Centre.Sigma.Ang = DoG.Centre.Sigma.Pix / PPA
  DoG.Centre.Kernel = gen_gaussian_kernel(DoG.Size.Pix, DoG.Centre.Sigma.Pix)

  # Define surround

  DoG.Surround.Sigma.Pix = Sigmas[1]
  DoG.Surround.Sigma.Ang = DoG.Surround.Sigma.Pix / PPA
  DoG.Surround.Kernel = gen_gaussian_kernel(DoG.Size.Pix, DoG.Surround.Sigma.Pix)

  # Difference of gaussians, depending on whether ON-Centre OFF-Surround or OFF-Centre ON-Surround

  if OnOff == "on":
    DoG.Kernel = DoG.Centre.Kernel - DoG.Surround.Kernel
  if OnOff == "off":
    DoG.Kernel = -DoG.Centre.Kernel + DoG.Surround.Kernel

  # Normalization, sum-to-zero

  DoG.Kernel = DoG.Kernel - np.mean(DoG.Kernel)

  # Normalization, max output =1

  inputMin = 0
  inputMax = 1

  # DoG.Kernel /= (np.sum(np.abs(DoG.Kernel)) / 2) * (inputMax - inputMin)

  return DoG