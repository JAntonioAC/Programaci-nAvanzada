I=imread('edc.jpg');
%figure;
imagesc(I);
I2=I+50,figure, image(I2)
I3=I-20;

subplot(3,1,1), image(I)
subplot(3,1,2), image(I2)
subplot(3,1,3), image(I3)