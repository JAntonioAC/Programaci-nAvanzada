import numpy as np
import cv2

#Configurar captura de cámara
cap = cv2.VideoCapture(0)

#Caras de frente
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while (True):
    ret, frame = cap.read() #lee el ojeto de la cámara
    #Transformar imagen a blanco y negro
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #Localizar cordenadas de rostros
    faces = face_cascade.detectMultiScale(gray,1.3, 5)
    
    #Enmarcar con rectángulo cada rostro
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        #Mostramos la imagen
        cv2.imshow('Frame',frame)
        #con la tecla q salimos del programa
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
