clear;
clc;

SerPIC = serial('COM5'); %Crea objeto COM
set(SerPIC,'BaudRate',9600); %define velocidad
set(SerPIC,'DataBits',8); %define numero de bits
serPIC.Terminator='none'; %Comunicacion constante sin caracter de terminacion
set(SerPIC,'Parity','none'); %Sin paridad
set(SerPIC,'StopBits',1); %numero de bits de stop 1
set(SerPIC,'FlowControl','none');%Sin control de hardware
fopen(SerPIC); %Abre objeto

for h=1:10
    x=fread(SerPIC,88);
    y=x;
    y=x(12:87)';
    v=0;
    i=0;
    k=1;
    for j=1:4:70
        i(k)=y(j).*256+y(j+1);
        v(k)=y(j+2).*256+y(j+3);
        k=k+1;
    end

    subplot(2,1,1);
    plot(v);
    subplot(2,1,2);
    plot(i);
    pause(.1);
 
end

fclose(SerPIC);
delete(SerPIC);
clear SerPIC;
