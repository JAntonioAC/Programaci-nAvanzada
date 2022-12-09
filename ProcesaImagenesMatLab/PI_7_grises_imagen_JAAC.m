I=imread('edc.jpg');

I2=I+50

%para cambiar grises
X=rgb2gray(I);
%figure;imshow(X);
h=[1 2 1;0 0 0; -1 -2 -1]; %coeficientes filtro
I2=filter2(h,X);%filtro la imagen en grises
subplot(2,1,1), imshow(X,[]),colorbar,title('grises');
subplot(2,1,2), imshow(I2,[]),colorbar,title('grises');