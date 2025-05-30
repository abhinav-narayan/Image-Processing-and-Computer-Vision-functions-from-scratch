# -*- coding: utf-8 -*-
"""
Created on Wed May 21 16:34:20 2025


This code performs rotation of an image without using numpy, opencv

@author: Abhi
"""

# import numpy as np
# import cv2  # for I/O only

def rotate_90(image):
    w = len(image)
    h = len(image[0])
    
    rotated = [[0 for _ in range(w)] for _ in range(h)]

    for i in range(h):
        for j in range(w):
            
            rotated[j][h - 1 - i] = image[i][j]

    return rotated

def rotate_180(image):
    w = len(image)
    h = len(image[0])
    rotated = [[0 for _ in range(w)] for _ in range(h)]

    for i in range(h):
        for j in range(w):
            rotated[h - 1 - i][ w - 1 - j] = image[i][j]

    return rotated



t = rotate_90([   
                   [1,2,3],
                   [4,5,6],
                   [7,8,9]
                   ])


t1 = rotate_180([
                   [1,2,3],
                   [4,5,6],
                   [7,8,9]
                   ])