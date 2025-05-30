# -*- coding: utf-8 -*-
"""
Created on Tue May 20 10:15:38 2025

@author: Abhi
"""



def histogram_equalization(image):
    """
    Performs histogram equalization on a 2D grayscale image of any size and intensity range.

    Args:
        image: A 2D list representing a grayscale image.

    Returns:
        A 2D list representing the equalized grayscale image (values scaled to 0–255).
    """
    height = len(image)
    width = len(image[0])
    total_pixels = height * width

    # Step 1: Find min and max intensity in the image
    min_val = min(min(row) for row in image)
    max_val = max(max(row) for row in image)
    intensity_range = max_val - min_val + 1

    # Step 2: Compute histogram
    histogram = [0] * intensity_range
    for row in image:
        for pixel in row:
            histogram[pixel - min_val] += 1

    # Step 3: Compute CDF
    cdf = [0] * intensity_range
    cdf[0] = histogram[0]
    for i in range(1, intensity_range):
        cdf[i] = cdf[i - 1] + histogram[i]

    cdf_min = next(c for c in cdf if c > 0)

    # Step 4: Equalization mapping (output scaled to 0–255)
    equalization_map = [0] * intensity_range
    for i in range(intensity_range):
        equalization_map[i] = round((cdf[i] - cdf_min) / (total_pixels - cdf_min) * 255)

    # Step 5: Apply mapping to image
    equalized_image = [
        [equalization_map[pixel - min_val] for pixel in row]
        for row in image
    ]

    return equalized_image

image = [
    [0, 2, 3, 2],
    [4, 5, 6, 7],
    [6, 4, 2, 3],
    [8, 9, 10, 16]
]

equalized = histogram_equalization(image)
for row in equalized:
    print(row)
