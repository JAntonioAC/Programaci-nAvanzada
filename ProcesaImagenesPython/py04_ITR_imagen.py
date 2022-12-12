#importar paquetes math, OpenCV y numpy
import math
import cv2
import numpy as np

#Abrir y mostrar imagen original
src=cv2.imread('game_time.jpg')
cv2.imshow('Original',src)

#Interpolación o escalamiento
dst = cv2.resize(src, (200,200), interpolation=cv2.INTER_CUBIC)
#Mostrar imagen escalada
cv2.imshow('Escalada',dst)

dst = cv2.resize(src, None, fx=0.70, fy=0.70, interpolation=cv2.INTER_CUBIC)
cv2.imshow('Escalada2',dst)

#Traslación
M = np.float32([[1, 0, 100],[0, 1, 50]])
dst = cv2.warpAffine(src, M, (512 + 100, 512 + 50))
#Mostrar imagen Trasladada
cv2.imshow('Traslation', dst)

#Rotación
rows, cols = src.shape[:2]

M = cv2.getRotationMatrix2D((cols / 2, rows), 45, 1)
dst = cv2.warpAffine(src, M, (cols, rows))
#Mostrar rotación
cv2.imshow ('Rotation', dst)

cv2.waitKey()
