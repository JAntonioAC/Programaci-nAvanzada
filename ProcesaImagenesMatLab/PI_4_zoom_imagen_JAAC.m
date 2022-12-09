I=imread('edc.jpg');
x=I(1:150,40:120,:);
subplot(1,2,1); subimage(I); title('original');
subplot(1,2,2); subimage(x); title('acercamiento');