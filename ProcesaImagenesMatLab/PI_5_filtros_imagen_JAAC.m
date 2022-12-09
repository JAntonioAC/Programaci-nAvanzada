I=imread('edc.jpg');

%para filtrar
h1=fspecial('gaussian');
h2=fspecial('log');
h3=fspecial('unsharp');
a=imfilter(I,h1);
b=imfilter(I,h2);
c=imfilter(I,h3);
subplot(2,2,1); subimage(I); title('original');
subplot(2,2,2); subimage(a); title('gaussian');
subplot(2,2,3); subimage(b); title('log');
subplot(2,2,4); subimage(c); title('unsharp');