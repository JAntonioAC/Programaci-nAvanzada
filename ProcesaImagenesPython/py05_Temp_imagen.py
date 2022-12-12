#importar paquetes math, OpenCV y numpy
import math
import cv2
import numpy as np

#Abrir imagen original
img=cv2.imread('game_time.jpg')

rows, cols = img.shape[:2]
#kernel_identity = np.array([[0,0,0], [0,1,0], [0,0,0]])
kernel_identity = np.array([[0,0,0], [0,0,1], [0,0,-1]])
#kernel_identity = np.array([[0,0,1,0,1], [0,0,0,0,0], [0,0,0,0,10]])
kernel_3x3 = np.ones((3,3), np.float32) /9.0
#kernel_5x3 = np.ones((5,5), np.float32) /25
kernel_5x5 = np.ones((7,7), np.float32) /25

#mostrar imagen original
cv2.imshow('Original', img)
output = cv2.filter2D(img, -1, kernel_identity)
cv2.imshow('filtro de indentidad', output)
output = cv2.filter2D(img, -1, kernel_3x3)
cv2.imshow('filtro de 3x3', output)
output = cv2.filter2D(img, -1, kernel_5x5)
cv2.imshow('filtro de 5x5', output)
cv2.waitKey(0)
