# -Girar a imagem 90 graus
# -Inverter a imagem (horizontal/vertical)
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carrega a imagem
img = cv2.imread('images/cria.png')
cv2.imshow('Imagem Original', img)

# Girar a imagem 90 graus
img_rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Imagem Girada 90 graus', img_rotated)

# Inverter a imagem
img_flipped = cv2.flip(img, 1)
cv2.imshow('Imagem Invertida Horizontal', img_flipped)
cv2.waitKey(0)