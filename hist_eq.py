# -*- coding: utf-8 -*-
"""
Created on Fri May 30 13:19:55 2025

@author: Abhi
"""

import numpy as np


def hist_eq_no_cv2(img_gray):

    m,n = img_gray.shape

    #Final output image - A zero padded image which will be remapped as shown in line 71
    hist_op = np.zeros((m,n),dtype = 'uint8')
    L = 2**(m)
    #To find frequency of pixel occurrances include an array of zeros
    cnts = np.zeros([L],dtype = 'int32')
    # print(cnts.shape)

    #Using arange syntax as opposed to linspace, will give you whole number 
    bins = np.arange(0,L)
    # print(bins) - Shows bins numbered from 0-255 with whole numbers

    for i in range(m):
        for j in range(n):
            # Counting the frequency of pixel intensities is done by finding the given intensity value and adding it by 1 until

            cnts[img_gray[i,j]] = cnts[img_gray[i,j]] + 1

    # print(cnts)

    #Computing Probability Distribution function
    no_of_pixels = m*n

    #Probability Distribution Function (PDF)
    p = np.zeros([L],dtype = 'float32')
    
    # Finding probability 
    for i in range(len(p)):
        p[i] = cnts[i]/no_of_pixels

    # print(np.sum(p))

    cdf = np.zeros([L],dtype = 'float32')

    # Mapping first value of Probability Distribution Function to Cumulative Distribution Function variable so that addition does not lead 
    # a sum of 2 as the maximum value. 1 is the maximum value of probability that can be obtained. 
    cdf[0] = p[0]

    # Function evaluates from 1-255 because we have defined cdf[0] <- p[0]
    for l in range(1,256):
        cdf[l] = cdf[l-1] + p[l]
    # print(cdf)

    #rounding off numbers - 0 is for whole number, whereas 1 means number rounded off with one decimal point
    #L - Number of Discrete intensity levels
    # L = 256
    sk = np.round(cdf * (L-1),0) #  Sk = (256 - 1) * cdf

    #Remapping of pixel intensities
    for M in range(m):
        for N in range(n):
            r = img_gray[M,N] # r - pixel intensity
            s = sk[r]  # s - cdf obtained at particular intensity value r as per input image
            hist_op[M,N] = s # Final output image remapped as per s
    return hist_op    
