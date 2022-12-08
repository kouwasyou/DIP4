"""
hist_equ() return the histogram equalization result of the input image.
Implement on RGB color image may lead to color distortion!!!
"""
import numpy as np

def hist_transform(Gsi_scr, G):
    [row, col] = Gsi_scr.shape
    Gs_he = np.arange(G)
    counts, bin_edges = np.histogram(Gsi_scr,np.arange(G+1))
    p_output = np.zeros((row,col),dtype=np.uint8)
    sum = 0
    for k in range(G):
        sum = sum+counts[k]
        Gs_he[k] = sum/(row*col)*(G-1)
    for i in range(row):
            for j in range(col):
                p_output[i, j] = Gs_he[Gsi_scr[i,j]]
    return p_output
    
    

def hist_equ(p_scr, Grayscal=256):  #return the histogram equalization of original picture p_scr
    if Grayscal != 256:
        print('Bit depth not 8!!!')
        return -1
    ndim = p_scr.shape   # Get the dimension of input picture
    if len(ndim) == 2:   # Picture has two dimension, grayscale
        return hist_transform(p_scr, Grayscal)
    elif len(ndim) == 3:  #Picture has three dimension, color image
        p_out = np.zeros(ndim,dtype=np.uint8)
        for i in range(3):
            p_out[:,:,i] = hist_transform(p_scr[:,:,i], Grayscal)
        return p_out
    else:
        print('Image dimension error!!!')
        return -2
