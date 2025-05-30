# -*- coding: utf-8 -*-
"""
Created on Tue May 13 10:35:44 2025

@author: Abhi
"""

def conv2d_no_npy(image, kernel):
    image_rows = len(image)
    image_cols = len(image[0])
    kernel_rows = len(kernel)
    kernel_cols = len(kernel[0])
    
    # Output dimensions (full convolution)
    out_rows = image_rows + kernel_rows - 1
    out_cols = image_cols + kernel_cols - 1
    
    # Initialize output with zeros
    output = [[0 for _ in range(out_cols)] for _ in range(out_rows)]
    
    # Perform convolution
    for i in range(out_rows):
        for j in range(out_cols):
            for m in range(kernel_rows):
                for n in range(kernel_cols):
                    if (i - m) >= 0 and (i - m) < image_rows and (j - n) >= 0 and (j - n) < image_cols:
                        output[i][j] += image[i - m][j - n] * kernel[m][n]
    
    return output

# Example image (3x3)
image = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Example kernel (2x2)
kernel = [
    [1, 0],
    [0, -1]
]

result = conv2d_no_npy(image, kernel)

# Print output
for row in result:
    print(row)

from scipy.signal import convolve2d

t = convolve2d(image, kernel)
print(t)