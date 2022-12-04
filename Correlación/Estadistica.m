entidad_um=COVID19MEXICO(:,1); 
sexo=COVID19MEXICO(:,2);
edad=COVID19MEXICO(:,3); 
tabaquismo=COVID19MEXICO(:,4); 
r_antigeno=COVID19MEXICO(:,5); 

media_edad=mean(edad) 
max_edad=max(edad) 
min_edad=min(edad)
moda_edad=mode(edad)
mediana_edad=median(edad)
desv_edad=std(edad)

for i=1:10000
    if entidad_um(i)==97;
        entidad_um(i)=0;
    end
    if entidad_um(i)==98; %if c(i)~=97;
        entidad_um(i)=0;
    end
    if entidad_um(i)==99;
        entidad_um(i)=0;
    end
end

for i=1:10000
    if sexo(i)==99;
        sexo(i)=0;
    end   
end

for i=1:10000
    if tabaquismo(i)==97;
        tabaquismo(i)=0;
    end
    if tabaquismo(i)==98; %if c(i)~=97;
        tabaquismo(i)=0;
    end
    if tabaquismo(i)==99;
        tabaquismo(i)=0;
    end
end

for i=1:10000
    if r_antigeno(i)==97;
        r_antigeno(i)=0;
    end   
end

CR1=corrcoef(entidad_um,r_antigeno)
CR2=corrcoef(sexo,r_antigeno)
CR3=corrcoef(edad,r_antigeno)
CR4=corrcoef(tabaquismo,r_antigeno)

figure
subplot(221),heatmap(CR1)
subplot(222),heatmap(CR2)
subplot(223),heatmap(CR3)
subplot(224),heatmap(CR4)