# -*- coding: utf-8 -*-
"""
Created on Wed May 14 19:43:33 2025

@author: Abhi
"""

import numpy as np

import numpy as np

def dft_1d(signal, N):
    N0 = len(signal)
    if N0 < N:
        signal = signal + [0] * (N - N0)
    else:
        signal = signal[:N]
    
    output = []
    for n in range(N):
        Xn = 0
        for k in range(N):
            Xn += signal[k] * np.exp(-2j * np.pi * n * k / N)
        output.append(Xn)
    return output

def dft_2d(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Apply 1D DFT on rows
    row_dft = []
    for row in matrix:
        row_dft.append(dft_1d(row, cols))
    
    # Transpose to apply DFT on columns
    row_dft_T = list(map(list, zip(*row_dft)))  # transpose

    # Apply 1D DFT on columns (which are rows now)
    col_dft = []
    for col in row_dft_T:
        col_dft.append(dft_1d(col, rows))

    # Transpose back to get final 2D DFT result
    dft2d = list(map(list, zip(*col_dft)))
    return dft2d

# Example 2D input (e.g., image matrix)
input_matrix = [
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1]
]

result = dft_2d(input_matrix)

t = np.fft.fft2(input_matrix)