# -Processamento de Cores:  separação de canais R, G e B
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carrega a imagem
img = cv2.imread('images/RGB.png')
cv2.imshow('Imagem Original', img)
cv2.waitKey(0)

# Separa os canais de cores
b, g, r = cv2.split(img)

# Exibe os canais de cores
cv2.imshow('Canal Vermelho', r)
cv2.imshow('Canal Verde', g)
cv2.imshow('Canal Azul', b)
cv2.waitKey(0)


