I=imread('edc.jpg');
K=imrotate(I,45);
subplot(1,2,1); subimage(I); title('original');
subplot(1,2,2); subimage(K); title('rotada');