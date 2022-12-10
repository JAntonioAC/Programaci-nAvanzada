import cv2
import numpy as np
img=cv2.imread('game_time.jpg')

b=img[100:500,100:500,1]
c=b.T #traspuesta
cv2.imshow('recorte',b)
cv2.imshow('traspuesta',c)
cv2.waitKey()
