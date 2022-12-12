#importar paquetes OpenCV y numpy
import cv2
import numpy as np

#Abrir la imagen
img=cv2.imread('game_time.jpg')
img
img.ndim

#Aplicar filtro de colores
a=img+5
b=img[:,:,1]
c=img[:,:,2]
d=b-c

#Mostrar imagenes modificadas
cv2.imshow('Sumando',a)
cv2.imshow('Solo rojos',b)
cv2.imshow('Solo verdes',c)
cv2.imshow('Resta',d)
cv2.waitKey()
