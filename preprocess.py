import cv2
import numpy as np

def preprocess_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Denoising: Reduce image noise using GaussianBlur
    blurred = cv2.GaussianBlur(img, (5, 5), 0)

    # Adaptive thresholding for better contrast and clearer lines
    binarized = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    # Morphological closing operation to clean small imperfections
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    cleaned = cv2.morphologyEx(binarized, cv2.MORPH_CLOSE, kernel, iterations=2)

    return cleaned
