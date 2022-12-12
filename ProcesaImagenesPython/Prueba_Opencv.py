# Importing OpenCV package
import cv2
import numpy as np

# Loading the required haar-cascade xml classifier file
#haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Reading the image
imge = cv2.imread('personas.jpg')

# Converting image to grayscale
gray = cv2.cvtColor(imge, cv2.COLOR_BGR2GRAY)

# Applying the face detection method on the grayscale image
#faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9)
faces = faceClassif.detectMultiScale(gray,
                                scaleFactor=1.01,
                                minNeighbors=10,
                                minSize=(30,30),
                                maxSize=(200,200))

# Iterating through rectangles of detected faces
for (x, y, w, h) in faces:
	cv2.rectangle(imge, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('Detected faces', imge)
cv2.waitKey(0)
