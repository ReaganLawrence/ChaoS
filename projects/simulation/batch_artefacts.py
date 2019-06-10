# -*- coding: utf-8 -*-
"""
Process 2D slices and produce turbulent artefacts

Created on Wed Nov 21 10:28:15 2018

@author: uqscha22
"""
#get list of images
import filenames
#load modules for arrays and nifti file support
import numpy as np
import nibabel as nib
import finite
import scipy.fftpack as fftpack
import pyfftw

#plot slices responsible for reconstruction
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm 

# Monkey patch in fftn and ifftn from pyfftw.interfaces.scipy_fftpack
fftpack.fft2 = pyfftw.interfaces.scipy_fftpack.fft2
fftpack.ifft2 = pyfftw.interfaces.scipy_fftpack.ifft2
fftpack.fft = pyfftw.interfaces.scipy_fftpack.fft
fftpack.ifft = pyfftw.interfaces.scipy_fftpack.ifft

# Turn on the cache for optimum performance
pyfftw.interfaces.cache.enable()

N = 256
K = 2.4
path = "slices/" #3D volumes
outpath = "slices_artefact/"
output_prefix = "case_"
caseIndex = 0

#setup fractal
lines, angles, mValues, fractal, oversampling = finite.finiteFractal(N, K, sortBy='Euclidean', twoQuads=True)
mu = len(lines)
print("Number of finite lines:", mu)
print("Number of finite points:", mu*(N-1))

imageList, caseList = filenames.getSortedFileListAndCases(path, caseIndex, "*.nii.gz", True)
imageList, sliceList = filenames.getSortedFileListAndCases(path, caseIndex+1, "*.nii.gz", True)
#print(imageList)
#print(caseList)

def show_slices(slices):
    """ Function to display row of image slices """
    fig, axes = plt.subplots(1, len(slices))
    for i, slice in enumerate(slices):
        axes[i].imshow(slice.T, cmap="gray", origin="lower")

#process each 3D volume
count = 0
for image, case, sliceIndex in zip(imageList, caseList, sliceList):
    img = nib.load(image)
    print("Loaded", image)

    #get the numpy array version of the image
    data = img.get_data() #numpy array without orientation
    fdata = img.get_fdata()
    lx, ly, lz = data.shape
    print("Image shape:", data.shape)

##    slice_0 = fdata[26, :, :]
##    slice_1 = fdata[:, 30, :]
##    slice_2 = fdata[:, :, 0]
##
##    fig, axes = plt.subplots(1, 3)
##    axes[0].imshow(slice_0.T, cmap="gray", origin="lower")
##    axes[1].imshow(slice_1.T, cmap="gray", origin="lower")
##    axes[2].imshow(slice_2.T, cmap="gray", origin="lower")
##        
##    plt.suptitle("Center slices for EPI image")  # doctest: +SKIP
##    plt.show()

    slice0 = fdata[:, :, 0]
    fig, ax = plt.subplots(1, 2)
    ax[0].imshow(fractal, cmap="gray", origin="lower")
    
    #pad
    mid = int(N/2.0)
    midx = int(lx/2.0+0.5)
    midy = int(ly/2.0+0.5)
    newLengthX1 = mid - midx
    newLengthX2 = mid + midx
    newLengthY1 = mid - midy
    newLengthY2 = mid + midy
    newImage = np.zeros((N,N))
#    imageio.imcrop(data, N, m=0, center=True, out_dtype=np.uint32)
    newImage[newLengthX1:newLengthX2, newLengthY1:newLengthY2] = data[:,:,0]
    
    #2D FFT
    kSpace = fftpack.fft2(newImage) #the '2' is important
#    fftkSpaceShifted = fftpack.fftshift(kSpace)
    kSpace *= fractal
    artefactImage = fftpack.ifft2(kSpace) #the '2' is important
    artefactImage = np.real(artefactImage)

    #artefactImage = np.fliplr(artefactImage)
    #artefactImage = np.flipud(artefactImage)
    artefactImage = np.swapaxes(artefactImage, 0, 1)

    ax[1].imshow(artefactImage, cmap="gray", origin="lower")
    plt.show()
 
    slice = nib.Nifti1Image(artefactImage, np.eye(4))
    outname = outpath + output_prefix + str(case).zfill(3) + "_slice_" + str(sliceIndex) + ".nii.gz"
    slice.to_filename(outname)
    count += 1
    
#    break
print("Total", count, "processed")
    
