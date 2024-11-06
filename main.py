#PPA refers to Pixels Per Arc, and is the measure of how many pixels correspond to a degree change in visual angle

PPA = np.array([8,8])

# Creating the Patch Size in both pixel and angular dimensions

PatchSize = Patch()
PatchSize.Pix = np.array([28,28])
PatchSize.Ang = np.array([8,8])

# Setting the dimensions of the kernel in both pixel and angular dimensions

tKSizeOFF = Kernel.OFF()
tKSizeOFF.Pix = np.array([9,9])
tKSizeOFF.Ang = np.ceil(tKSizeOFF.Pix / PPA)

# Setting the the dimensions of the centre and surround in both pixel and angular dimensions

tSigmaCentreSurroundOFF = SigmaCentreSurround.OFF()
tSigmaCentreSurroundOFF.Pix = np.array([(1/3) * tKSizeOFF.Pix[0], (2/3) * tKSizeOFF.Pix[0]])
tSigmaCentreSurroundOFF.Ang = tSigmaCentreSurroundOFF.Pix / PPA

# Using the above parameters, set the filter coefficients of the off-center kernel using a difference of gaussians

kernelOFF = DoG(tKSizeOFF.Pix, PPA, tSigmaCentreSurroundOFF.Pix, "off")

# Now, do the same for the on-center kernel

tKSizeON = Kernel.ON()
tKSizeON.Pix = tKSizeOFF.Pix
tKSizeON.Ang = np.ceil(tKSizeOFF.Pix / PPA)

tSigmaCentreSurroundON = SigmaCentreSurround.ON()
tSigmaCentreSurroundON.Pix = np.array([(1/3) * tKSizeON.Pix[0], (2/3) * tKSizeON.Pix[0]])
tSigmaCentreSurroundON.Ang = tSigmaCentreSurroundON.Pix / PPA

kernelON = DoG(tKSizeON.Pix, PPA, tSigmaCentreSurroundON.Pix, "on")

Trimsize = np.array([28,28])
SamplesPatch = np.array([28,28])

NFeatures = np.prod(SamplesPatch) * 2

ImSize = Image()
ImSize.Pix = np.array([28,28])
ImSize.Ang = [8,8]
