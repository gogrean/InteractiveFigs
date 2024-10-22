import pyfits
import numpy as np

def read_binmap(ImFile):
    hdu = pyfits.open(ImFile)
    hdr = hdu[0].header
    del hdr['COMMENT']
    del hdr['HISTORY']
    BinIm = hdu[0].data
    return BinIm, hdr

def filter_bin(im, bin):
    imcopy = im.copy()
    imcopy[im == bin] = 1
    imcopy[im != bin] = 0
    return imcopy
    
def find_bins(im):
    bins = []
    maxbin = np.max(im)
    [bins.append(i) for i in np.arange(1,maxbin+1) if i in im]
    return bins



