%cargar una imagen que debe estar en nuestra carpeta de trabajo
I=imread('edc.jpg');

%Para reducir el numero de colores
I2=I+50
image(I2)
I3=I-20;
subplot(2,2,1), subimage(I); title('Original');
[X_no, map]=rgb2ind(I,8,'nodither');
subplot(2,2,2), image(I2); title('Sin color');
[X_dit, map]=rgb2ind(I,8,'dither');
subplot(2,2,3), image(I3); title('Sin color2');