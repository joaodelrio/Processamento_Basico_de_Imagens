#-Conversão de colorido RGB para tons de cinza
#-Conversão de tons de cinza para preto e branco (limiarização/binarização manual)
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carrega a imagem
img = cv2.imread('images/cria.png')
cv2.imshow('Imagem Original', img)

# Converte a imagem para tons de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Imagem Cinza', gray)
cv2.waitKey(0)

# Limiarização/Binarização
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Imagem Binaria', thresh)

# ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow('Imagem Binaria Invertida', thresh)
# cv2.waitKey(0)

# Limiarização/Binarização manual
for i in range(gray.shape[0]):
    for j in range(gray.shape[1]):
        if gray[i, j] > 127:
            gray[i, j] = 255
        else:
            gray[i, j] = 0

cv2.imshow('Imagem Binaria Manual', gray)
cv2.waitKey(0)