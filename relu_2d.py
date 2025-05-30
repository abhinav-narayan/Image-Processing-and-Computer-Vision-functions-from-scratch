# -*- coding: utf-8 -*-
"""
Created on Mon May 19 15:08:03 2025

@author: Abhi
"""

def relu_2d(image):
    output = []
    for row in image:
        new_row = []
        for pixel in row:
            new_row.append(pixel if pixel > 0 else 0)
        output.append(new_row)
    return output

# 2D image example
image = [[-10, 20, -5],
         [0, -2, 8]]

relu_output = relu_2d(image)
print(relu_output)


import math

def softmax_1d(logits):
    # For numerical stability, subtract max logit
    max_logit = max(logits)
    exps = [math.exp(x - max_logit) for x in logits]
    sum_exps = sum(exps)
    return [e / sum_exps for e in exps]

logits = [2.0, 1.0, 0.1]
probs = softmax_1d(logits)
print(probs)  # Output:[0.6590011388859679, 0.24243297070471392, 0.09856589040931818]