%Obesidad
a=COVID19MEXICO(:,4);
%Edad
b=COVID19MEXICO(:,3);
%Resultados
c=COVID19MEXICO(:,5);
%Sexo
d=COVID19MEXICO(:,2);
%entidad_um
e=COVID19MEXICO(:,1);

for i=1:10000
    if a(i)==98;
        a(i)=0;
    end
    if c(i)==97; %if c(i)~=97;
        c(i)=0;
    end
end

mediaA=mean(a)
medianaA=median(a)
desvstandA=std(a)
varianzaA=var(a)
covarianzA=cov(a)
%plot(a)

mediaA=mean(c)
medianaA=median(c)
desvstandA=std(c)
varianzaA=var(c)
covarianzA=cov(c)

CR1=corrcoef(a,b)
CR2=corrcoef(a,c)
CR3=corrcoef(b,c)
CR4=corrcoef(d,c)

figure
subplot(221),heatmap(CR1)
subplot(222),heatmap(CR2)
subplot(223),heatmap(CR3)
subplot(224),heatmap(CR4)