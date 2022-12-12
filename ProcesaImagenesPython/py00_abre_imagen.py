#importar paquetes OpenCV y numpy
import cv2
import numpy as np

#Abrir la imagen
img=cv2.imread('game_time.jpg')
img
img.ndim

#Mostrar la imagen
cv2.imshow('Mi escritorio', img)
cv2.waitKey(0)
