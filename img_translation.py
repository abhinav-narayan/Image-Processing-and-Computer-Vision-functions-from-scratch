# -*- coding: utf-8 -*-
"""
Created on Thu May 22 17:19:22 2025

@author: Abhi
"""

import numpy as np

def translate_image(image, dx, dy):
    h, w = image.shape[:2]
    
    # Create blank canvas
    translated = np.zeros_like(image)

    for i in range(h):
        for j in range(w):
            new_i = i + dy
            new_j = j + dx

            # Check if new position is inside bounds
            if 0 <= new_i < h and 0 <= new_j < w:
                translated[new_i, new_j] = image[i, j]

    return translated


img = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

t = translate_image(img, 1, 0)