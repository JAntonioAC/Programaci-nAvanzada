#importar paquetes OpenCV y numpy
import cv2
import numpy as np

#Abrir la imagen
img=cv2.imread('game_time.jpg')

#Mostrar la imagen
cv2.imshow('Original',img)

from matplotlib import pyplot as plt

#Modifica imagen en escala de grises
img = cv2.imread('game_time.jpg',cv2.IMREAD_GRAYSCALE)

#Mostrar una imagen modificada a escala de grises
cv2.imshow('Escala grises',img)

#Crear histograma de la imagen modificada a escala de grises
hist = cv2.calcHist([img],[0],None,[256],[0,256])

#Aplica color al histograma
plt.plot(hist, color='blue')
#Título del eje X
plt.xlabel('intensidad de iluminación')
#Título deleje Y
plt.ylabel('cantidad de pixeles')
#Mostrar histograma
plt.show()
