# -*- coding: utf-8 -*-
"""
Created on Fri May 23 11:13:22 2025

@author: Abhi
"""
import numpy as np

def maxpool2d(image, pool_size=2, stride=2):
    h, w = image.shape
    out_h = (h - pool_size) // stride + 1
    out_w = (w - pool_size) // stride + 1

    pooled = np.zeros((out_h, out_w), dtype=image.dtype)

    for i in range(out_h):
        for j in range(out_w):
            h_start = i * stride
            h_end = h_start + pool_size
            w_start = j * stride
            w_end = w_start + pool_size

            window = image[h_start:h_end, w_start:w_end]
            pooled[i, j] = np.max(window)

    return pooled

image = np.array([
    [1, 3, 2, 4],
    [5, 6, 7, 8],
    [4, 3, 2, 1],
    [0, 1, 3, 2]
], dtype=np.uint8)

pooled = maxpool2d(image, pool_size=2, stride=2)
print(pooled)