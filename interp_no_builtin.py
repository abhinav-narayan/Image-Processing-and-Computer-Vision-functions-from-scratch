# -*- coding: utf-8 -*-
"""
Created on Mon May 19 14:29:41 2025

Image interpolation without built in function

@author: Abhi
"""

import numpy as np
import matplotlib.pyplot as plt

def manual_resize(image, new_width, new_height):
    old_height, old_width = image.shape
    resized_image = np.zeros((new_height, new_width), dtype=np.uint8)

    for i in range(new_height):
        for j in range(new_width):
            # Map new pixel locations to old image coordinates
            x_old = min(int(j * old_width / new_width), old_width - 1)
            y_old = min(int(i * old_height / new_height), old_height - 1)

            # Assign the nearest pixel value
            resized_image[i, j] = image[y_old, x_old]

    return resized_image

# Without numpy -  using list
def img_interp(image,M,N):
    width = len(image)
    height = len(image[0])
    interp_op = [[0 for _ in range(M)] for _ in range(N)]
    
    for i in range(M):
        for j in range(N):
            x = min(int(j * width/M), width - 1)
            y = min(int(i * height/N), height - 1)
            interp_op[i][j] = image[y][x]
    
    return interp_op 

# Example: 2x2 image
img = np.array([[10, 20],
                [30, 40]], dtype=np.float32)

# Resize to 10x10
resized_img = manual_resize(img, 10, 10)

