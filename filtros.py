# -Filtros da Média
# -Filtro da Mediana
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carrega a imagem
img = cv2.imread('images/tigre.png')

# Converte para cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Imagem Cinza', gray)

# Cria uma cópia da imagem
img_mean = gray.copy()
img_median = gray.copy()

# Filtro da Média
for i in range(1, img_mean.shape[0] - 1):
    for j in range(1, img_mean.shape[1] - 1):
        img_mean[i, j] = np.mean(img_mean[i-1:i+2, j-1:j+2])
        

cv2.imshow('Imagem Filtro da Media', img_mean)
# Filtro da Mediana
for i in range(1, img_median.shape[0] - 1):
    for j in range(1, img_median.shape[1] - 1):
        img_median[i, j] = np.median(img_median[i-1:i+2, j-1:j+2])


# cv2.imshow('Imagem Filtro da Mediana', img_median)
cv2.waitKey(0)